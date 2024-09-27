from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name='my_home_view'), 
    path("map", MapView.as_view(), name='my_map_view'), 
]