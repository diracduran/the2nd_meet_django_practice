from django.contrib import admin
from lead.models import Lead

# Register your models here.
@admin.register(Lead)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message']
