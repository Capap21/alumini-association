# alumni/urls.py
from django.urls import path,include
from .views import home, about, register

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path("accounts/", include("django.contrib.auth.urls"))
]
