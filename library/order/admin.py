from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at')
    list_filter = ('created_at', 'end_at', 'plated_end_at')
    search_fields = ('user__email', 'book__title')
    ordering = ('-created_at',)
