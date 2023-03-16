from django.shortcuts import render


def view_bag(request):
    """A view to render shopping bag contents"""
    return render(request, 'bag/bag.html')
