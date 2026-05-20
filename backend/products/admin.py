from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display   = ('product_image', 'name', 'category', 'price', 'stock', 'is_featured', 'created_at')
    list_editable  = ('price', 'stock', 'is_featured')
    list_filter    = ('category', 'is_featured')
    search_fields  = ('name', 'description')
    list_per_page  = 20
    readonly_fields = ('created_at', 'updated_at', 'product_image')

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'category', 'description')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'stock', 'is_featured')
        }),
        ('Image', {
            'fields': ('image', 'product_image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def product_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:8px;" />', obj.image.url)
        return '—'
    product_image.short_description = 'Preview'
