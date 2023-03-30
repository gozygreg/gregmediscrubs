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

    # To view customer general reviews about our e-commerce company
    path('customer_reviews', views.customer_reviews, name='customer_reviews'),
    ]