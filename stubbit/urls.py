from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.login, name="login"),
    path("organization/", views.AddOrganization, name="organization"),
    path("createstub/", views.createstub, name="create stub")
]
