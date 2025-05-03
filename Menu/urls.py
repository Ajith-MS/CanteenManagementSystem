from django.urls import path
from .views import list_menu

app_name = "Menu"

urlpatterns = [
    path("list/", list_menu, name="listmenu"),
    # path("", user_signin, name="usersignin"),
]