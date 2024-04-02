"""
URL configuration for djangobackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from database.views import LinksAPI
from database import views
from website.urls import display_links

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/add_link/', add_link, name='add_link'),
    path('website/', display_links, name= 'display_links'),
    path('', display_links, name= 'display_links'),
    path('frontendAPI/', views.LinksAPI.as_view()),
]
