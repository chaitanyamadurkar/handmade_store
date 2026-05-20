from django.contrib import admin
from django.utils.html import format_html
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display   = ('id', 'customer_name', 'product_link', 'quantity',
                      'total_price', 'status_badge', 'status', 'created_at')
    list_filter    = ('status', 'created_at')
    search_fields  = ('customer_name', 'customer_email', 'customer_phone')
    list_editable  = ('status',)
    readonly_fields = ('total_price', 'created_at', 'updated_at')
    list_per_page  = 25

    fieldsets = (
        ('Customer Info', {
            'fields': ('customer_name', 'customer_email', 'customer_phone', 'address')
        }),
        ('Order Details', {
            'fields': ('product', 'quantity', 'total_price', 'notes')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def product_link(self, obj):
        return obj.product.name
    product_link.short_description = 'Product'

    def status_badge(self, obj):
        colors = {
            'pending':   '#f59e0b',
            'confirmed': '#3b82f6',
            'shipped':   '#8b5cf6',
            'delivered': '#22c55e',
            'cancelled': '#ef4444',
        }
        color = colors.get(obj.status, '#6b7280')
        return format_html(
            '<span style="background:{};color:white;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = 'Status'