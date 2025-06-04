from django.shortcuts import render, redirect
from .models import Menu
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import random
import os
# Create your views here.
def list_menu(request):
    # This is a placeholder view function for listing menu items.
    # You can implement the logic to fetch and display menu items here.
    list_items = Menu.objects.all()
    return render(request, "list_menu.html",{'items': list_items})


def generate_item_id():
    existing_ids = set(Menu.objects.values_list('item_id', flat=True))
    while True:
        random_id = f"{random.randint(1000, 9999):04d}"
        if random_id not in existing_ids:
            return random_id



def create_item(request):   
    if request.method == 'POST':
        # Handle the form submission to create a new menu item
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        category = request.POST.get("category")
        itemtype = request.POST.get("itemtype")
        image = request.FILES.get("image")
        availablity = request.POST.get("availablity")    
        item_id = generate_item_id()
        tags = request.POST.getlist("tags")

        # Get the file extension
        file_extension = os.path.splitext(image.name)[1]
        # Create new filename with item_id
        new_filename = f"{item_id}{file_extension}"
        # Save the file with the new name
        file_path = default_storage.save(f'menu_images/{new_filename}', ContentFile(image.read()))

        
        # Create a new Menu object with the saved file path
        Menu.objects.create(
            item_id=item_id,
            name=name,
            price=price,
            quantity=quantity,
            category=category,
            itemtype=itemtype,
            image=file_path,
            availablity=availablity,
            tags=tags
        )
        # Redirect to the list menu page after creating the item
        return redirect('Manager:list_menu')
    return render(request, "create_item.html")

def edit_item(request, item_id):
    # Handle the form submission to edit an existing menu item
    item = Menu.objects.get(item_id=item_id)

    if request.method == 'POST':
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.quantity = request.POST.get("quantity")
        item.category = request.POST.get("category")
        item.itemtype = request.POST.get("itemtype")
        item.availablity = request.POST.get("availablity")
        item.tags = request.POST.getlist("tags")

        # Check if a new image is uploaded
        if 'image' in request.FILES:
            image = request.FILES['image']
            # Get the file extension
            file_extension = os.path.splitext(image.name)[1]
            # Create new filename with item_id
            new_filename = f"{item.item_id}{file_extension}"
            # Save the file with the new name
            file_path = default_storage.save(f'menu_images/{new_filename}', ContentFile(image.read()))
            item.image = file_path
        # Save the updated item
        item.save()
        return redirect('Manager:listmenu')
    return render(request, "edit_item.html", {'item': item})

def delete_item(request, item_id):
    # Handle the deletion of a menu item
    item = Menu.objects.get(item_id=item_id)
    if request.method == 'POST':
        item.delete()
    return redirect('Manager:list_menu')
