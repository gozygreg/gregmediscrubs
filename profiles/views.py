from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully')
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        'form': form,
        'order': orders,
        'on_profile_page': True
    }

    return render(request, 'profiles/profile.html', context)