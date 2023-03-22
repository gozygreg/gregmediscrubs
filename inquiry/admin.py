from django.contrib import admin
from .models import CustomerInquiry, InternalCommunicationNotes


class InternalCommunicationNotesAdmin(admin.StackedInline):
    """
    Internal notes for staff when replying to customers
    messages via email
    """

    model = InternalCommunicationNotes
    extra = 1
    verbose_name_plural = 'Internal Communication Notes'
    verbose_name = 'Internal Communication Note'
    fields = ('notes', 'date',)
    readonly_fields = ('date',)
    can_delete = False


@admin.register(CustomerInquiry)
class CustomerInquiryAdmin(admin.ModelAdmin):
    """
    Allows staff to view/filter customer messages
    but prevents the content being changed
    """

    inlines = (InternalCommunicationNotesAdmin,)
    baseModel = CustomerInquiry
    list_display = (
        'date_received',
        'name',
        'email',
        'subject',
        'pending_reply',
        'marked_as_done',
    )
    list_filter = ('pending_reply', 'marked_as_done', 'date_received')
    search_fields = ('name', 'email', 'subject', 'inquiry',)
    summer_note_field = ('inquiry',)
    readonly_fields = ('date_received', 'inquiry',)

    ordering = ('-date_received',)