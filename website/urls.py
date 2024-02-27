from django.urls import path
from .views import display_links

urlpatterns = [
    path('links/', display_links, name='display_links'),
]
