from django.shortcuts import render
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your shoppimg bag is empty')
        return redirect(reverse('store'))
    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MX7x2AGFYQzGfhGw5CWd6b1MlJ3C11whROQsiK8AcK31fXPYq35F7kgNlZBwE8wRpjIAyrYjeLwOgYqY6YnRsEK00JcAoHlHd',
        'client_secret': 'test client secret',
        }
    return render(request, 'checkout/checkout.html', context)
