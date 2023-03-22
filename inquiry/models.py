from django.db import models


# Create your models here.
class CustomerInquiry(models.Model):
    date_received = models.DateTimeField(auto_now_add=True)
    name = models.CharField(null=False, blank=False, max_length=50)
    email = models.EmailField(null=False, blank=False, max_length=254)
    subject = models.CharField(max_length=254)
    inquiry = models.TextField(null=False, blank=False,)
    pending_reply = models.BooleanField(default=True)
    marked_as_done = models.BooleanField(default=False)

    def __str__(self):
        return f" message from {self.email}"

    class Meta:
        verbose_name_plural = "Customer Inquiries"


class InternalCommunicationNotes(models.Model):
    """
    Model to store internal notes for customer messages
    """

    related_inquiry = models.ForeignKey(CustomerInquiry, on_delete=models.CASCADE, related_name='related_message')
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return f'Internal notes for message id no. {self.related_inquiry.id}'
