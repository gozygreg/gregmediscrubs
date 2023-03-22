from django.shortcuts import render
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import InquiryForm


class Inquiry(SuccessMessageMixin, CreateView):
    """"
    Handles the contact form display and submission
    """
    form_class = InquiryForm
    template_name = './inquiry/inquiry.html'
    success_url = reverse_lazy('inquiry')
    success_message = 'We have received your inquiries.\
        We will get back to you shortly.'

    def form_valid(self, form):
        """
        Validates form data
        """

        form.save()
        return super().form_valid(form)


