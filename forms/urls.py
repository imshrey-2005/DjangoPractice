from django.contib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    path('/',views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.success_view, name='success'),
]
