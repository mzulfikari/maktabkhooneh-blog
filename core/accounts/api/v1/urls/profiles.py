from django.urls import path, include
from .. import views

# profile
urlpatterns = [path("", views.ProfileApiView.as_view(), name="profile")]
