from django.urls import path
from .views import list_menu, create_item, edit_item, delete_item
app_name = "Manager"

urlpatterns = [
    path("list/", list_menu, name="list_menu"),
    path("create/", create_item, name="create_item"),
    path("edit/<int:item_id>/", edit_item, name="edit_item"),
    path("delete/<int:item_id>/", delete_item, name="delete_item")
]