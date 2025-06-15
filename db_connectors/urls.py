from django.urls import path
from . import views

app_name = 'db_connectors'
urlpatterns = [
    path('pf_jobs/', views.pf_jobs_detail, name='pf_jobs_detail'),
    path('failed_builds/', views.failed_builds_dashboard, name='failed_builds_dashboard'),
    path('warehouse/<str:warehouse_id>/variants/', views.warehouse_variants, name='warehouse_variants'),
]