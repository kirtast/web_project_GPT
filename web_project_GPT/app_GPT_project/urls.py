from django.urls import path
from . import views

# Define URL patterns for this app
urlpatterns = [
    # Home page URL pattern, maps to the 'home' function in views.py
    path('', views.home, name='home'),
    
    # About page URL pattern, maps to the 'about' function in views.py
    path('about/', views.about, name='about'),
    
    # Contact page URL pattern, maps to the 'contact' function in views.py
    path('contact/', views.contact, name='contact'),
]
