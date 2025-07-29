from django.contib import admin
from django.urls import path

urlpatterns = [
    # Define your URL patterns here
    path('forms/',admin.site.urls),
]
