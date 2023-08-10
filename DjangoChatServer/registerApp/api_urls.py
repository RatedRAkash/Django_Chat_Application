from django.urls import path
from registerApp.api_views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # These are for FRONTEND(Vue, React) APIs
    path('signup', UserRegistrationAPIView.as_view(), name='signup'),
    path('login', UserLoginAPIView.as_view(), name='login'),
    path('logout', UserLogoutAPIView.as_view(), name='logout'),

    # JWT(Json Web Token) Url Paths
    path('gettoken', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken', TokenVerifyView.as_view(), name='token_verify'),
]