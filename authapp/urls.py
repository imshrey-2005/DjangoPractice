from django.urls import path
from . import views
urlpatterns = [
    path('', views.SignUpView, name='signup'),  # URL for user signup
]