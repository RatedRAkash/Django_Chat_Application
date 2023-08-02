from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.FrontPageView.as_view(), name='frontpage'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registerApp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
