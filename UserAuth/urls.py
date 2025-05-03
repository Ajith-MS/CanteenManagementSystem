from django.urls import path
from UserAuth.views import user_signUp

urlpatterns = [
    path("signup/", user_signUp, name="usersignup"),
]