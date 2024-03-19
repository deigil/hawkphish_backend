from django.urls import path
from . import views
from .views import getData, postData

from django.conf import settings

urlpatterns = [
    # path('', getData),
    # path('post/', postData, name='post_data'),
    path('frontendAPI/', views.LinksAPI.as_view()),
]
