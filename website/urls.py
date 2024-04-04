from django.urls import path
from website.views import display_links
from .views import display_links
from . import views
from django.conf import settings
from .views import homepage

urlpatterns = [
    # path('links/', display_links, name='display_links'),
    path('', homepage, name='homepage'),
    path('static/<path:path>', settings.STATIC_URL + '/<path:path>'),
]
