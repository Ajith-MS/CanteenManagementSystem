from django.urls import path
from .views import menu
app_name = "Home"

urlpatterns = [
    path("", menu, name="menulist"),
]