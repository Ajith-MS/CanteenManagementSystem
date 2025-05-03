from django.urls import path
from UserAuth.views import user_signUp

urlpatterns = [
    path("signUp/", user_signUp, name="usersignup"),  
]