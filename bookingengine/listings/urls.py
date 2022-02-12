# Urls for selfprep api



from django.urls import path

from .views import   get_available_listings

urlpatterns = [
    
    path('units/',get_available_listings),
    
    
]
