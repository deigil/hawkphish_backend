from django.urls import path
from website.views import display_links
from .views import display_links
from . import views
from django.conf import settings
from .views import homepage
from django.conf.urls.static import static

urlpatterns = [
    # path('links/', display_links, name='display_links'),
    path('', homepage, name='homepage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
