from django.urls import path
from .views import *

urlpatterns = [
    path("", MapView.as_view(), name='my_map_view'), 
]