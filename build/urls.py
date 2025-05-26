# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.build_homepage, name='build_homepage'),
    path('products/', views.product_list, name='product_list'),
    path('products/<str:product_name>/', views.product_build_details, name='product_build_details'),
    path('wonnect_kernel_tips/', views.get_wonnect_and_kernel_tips, name='get_wonnect_and_kernel_tips'),
]