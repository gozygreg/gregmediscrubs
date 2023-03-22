from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inquiry.as_view(), name='inquiry'),
]