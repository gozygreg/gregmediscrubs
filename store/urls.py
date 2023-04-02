from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='store'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

    # To submit review about a product (Product-review)
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),

    # To view customer testimonials about our e-commerce company
    path('testimonial_list/', views.testimonial_list, name='testimonial_list'),
    path('testimonial_detail/<int:pk>/', views.testimonial_detail, name='testimonial_detail'),
    path('testimonial_add/', views.add_testimonial, name='add_testimonial'),
    path('testimonial_edit/<int:pk>/', views.edit_testimonial, name='edit_testimonial'),
    path('testimonial_delete/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),
]