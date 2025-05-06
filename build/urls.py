# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<str:product_name>/', views.product_build_details, name='product_build_details'),
]