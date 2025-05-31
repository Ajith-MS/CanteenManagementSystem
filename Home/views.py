from django.shortcuts import render
from Manager.models import Menu

# Create your views here.
def menu(request):
    listmenu = Menu.objects.all()
    return render(request, "home.html", {'items': listmenu})

