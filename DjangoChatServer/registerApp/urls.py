from django.contrib.auth import views as auth_views
from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    # These are for DJANGO Native Views
    path('', views.FrontPageView.as_view(), name='frontpage'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registerApp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]