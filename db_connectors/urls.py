from django.urls import path
from . import views

app_name = 'db_connectors'
urlpatterns = [
    path('pf_jobs/', views.pf_jobs_detail, name='pf_jobs_detail'),
]