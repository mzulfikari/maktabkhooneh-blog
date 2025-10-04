from django.urls import path,include
from .. import views
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # registration
    path("registration/",views.RegistrationApiView.as_view(),name="registration"),
    # login token
    path("token/login",views.CustomAuthToken.as_view(),name="login-token"),
    # activation
    path("test/email",views.TestEmailSend.as_view(),name="login-token"),
    #path('activation/confirm)
    # resend activation
    # change password
    path("change-password/",views.ChangePasswordApiView.as_view(),name='change-password'),
    # reset password 
    # login jwt
    path('jwt/create/',TokenObtainPairView.as_view(),name='jwt-cerate'),
    path('jwt/refresh/',TokenRefreshView.as_view(), name='jwt_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]
