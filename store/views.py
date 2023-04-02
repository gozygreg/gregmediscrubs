from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ReviewRating
from checkout.models import Order, OrderLineItem
from .forms import ProductForm, ReviewForm
from django.contrib.auth.models import User


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria")
                return redirect(reverse('store'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'store/store.html', context)


@login_required
def product_detail(request, product_id):
    """ A view to individual product details """

    product = get_object_or_404(Product, pk=product_id)

    try:
        order_line_item = OrderLineItem.objects.filter(product=product, order__user_profile=request.user.userprofile)
        # Check if the product is in any order
        if order_line_item.exists():
            order = order_line_item[0].order
        else:
            order = None
    except OrderLineItem.DoesNotExist:
        order = None

    # Get the review
    reviews = ReviewRating.objects.filter(product=product, status=True)

    context = {
        'product': product,
        'order': order,
        'reviews': reviews,
        }

    return render(request, 'store/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store via the frontend """
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can add product to site')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added to store successfully')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failled. Check form validity')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'store/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can edit a product')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} updated successfully')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.info(request, f'Product update failure. Check form validaity')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'{product.name} is being edited')
    context = {'form': form, 'product': product}
    return render(request, 'store/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """ delete a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can delete a product')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'product deleted!')
    return redirect(reverse('store'))


@login_required
def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you. Your review is updated')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted')
                return redirect(url)


def customer_testimonials(request):
    return render(request, 'store/customer_testimonials.html')
