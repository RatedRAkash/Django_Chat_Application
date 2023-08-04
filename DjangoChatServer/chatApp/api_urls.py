from . api_views import *
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api_views import *

player_router = DefaultRouter()

urlpatterns = [
    #  ***************** API Routes ******************

    #  ***************** "api/" Prefix is already defined in MainApp of Django Project ******************
    # Destination API
    path('rooms', AllRoomsApiView.as_view(), name = AllRoomsApiView.api_name),
]