from .models import CustomerInquiry
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget


class InquiryForm(ModelForm):
    """
    Form to handle inquiry form submission
    """
    class Meta:
        model = CustomerInquiry
        fields = ('name', 'email', 'subject', 'inquiry')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Initialise the form attributes
        """

        placeholders = {
            'name': 'Name',
            'email': 'Email address',
            'subject': 'Subject',
            'inquiry': 'Inquiry/Testimonial',
        }

        self.fields['name'].widget.attrs['autofocus'] = True

        for field in self.fields:

            if self.fields[field].required:

                placeholder = f'{placeholders[field]} *'

            else:

                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'aria-label'] = placeholder
            self.fields[field].label = False