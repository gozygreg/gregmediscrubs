from django.contrib import admin
from .models import Product, Category, ReviewRating, Testimonial


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'image_url'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'image')
    readonly_fields = ('author',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ReviewRating)
admin.site.register(Testimonial, TestimonialAdmin)
