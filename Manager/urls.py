from django.urls import path
from .views import list_menu, create_item, edit_item
app_name = "Manager"

urlpatterns = [
    path("list/", list_menu, name="listmenu"),
    path("create/", create_item, name="createitem"),
    path("edit/<int:item_id>/", edit_item, name="edititem"),
]