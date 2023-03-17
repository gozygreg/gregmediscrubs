from django.shortcuts import render
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your shoppimg bag is empty')
        return redirect(reverse('store'))
    order_form = OrderForm()
    context = {'order_form': order_form,}
    return render(request, 'checkout/checkout.html', context)
