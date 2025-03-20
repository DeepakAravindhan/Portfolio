# contact_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),
    path('contact/', views.contact_form, name='contact_form'),
]