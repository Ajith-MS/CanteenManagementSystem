from django.urls import path
from .views import user_signup, user_signin

app_name = "UserAuth"

urlpatterns = [
    path("signup/", user_signup, name="usersignup"),
    path("signin/", user_signin, name="usersignin"),
]