from django.urls import path
from .views import display_links
from . import views
from django.conf import settings

urlpatterns = [
    path('links/', display_links, name='display_links'),
]
