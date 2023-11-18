# officesharingapi/urls.py

from django.urls import path
from .views import registration_view, login_view, homepage_view  # Import your registration view
from . import views
urlpatterns = [
    # Add other URL patterns as needed
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),    
    path('homepage/', homepage_view, name='homepage_view'),
]
