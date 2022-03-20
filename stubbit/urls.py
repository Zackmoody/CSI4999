from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.login, name="login"),
    path("organization/", views.AddOrganization, name="organization"),
    path("createstub/", views.createstub, name="createstub"),
    path("refresh/", views.refresh, name="refresh"),
    path("login_message_homeredirect/", views.loginwelcome, name="loginwelcome"),
    path("addOrganization_message_homeredirect/", views.addOrganizationSuccess, name="addOrganizationSuccess"),
    path("createStub_message_homeredirect/", views.addStubSuccess, name="addStubSuccess"),
    path("signupsuccess/", views.signupsuccess, name="signupsuccess"),
    path("about/", views.about, name="about")
]
