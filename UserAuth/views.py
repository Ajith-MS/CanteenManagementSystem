from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect   
from django.contrib.auth import get_user_model
from UserAuth.models import CustomUser  
from django.contrib.auth import authenticate, login 
from django.http import JsonResponse
import json

# Create your views here.
def user_signup(request):  
    User = get_user_model()
    all_user = User.objects.values_list("username", flat=True)
    all_numbers = CustomUser.objects.values_list("phone_number", flat=True)
    all_emails = User.objects.values_list("email", flat=True)
    if request.method == 'POST':
        user_name = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")  
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")


        # Check if the username is already taken
        if user_name in all_user:
            messages.error(request, "Username already exists!!")

        # Check if the email is already taken
        elif email in all_emails:
            messages.error(request, "Email already exists!!")

        # Check if the phone number is already taken
        elif phone_number in all_numbers:
            messages.error(request, "Phonenumber already exists!!")\
            
        else:
            # create a new user
            User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email, password=password, phone_number=phone_number)
            messages.success(request, "Account created successfully")
            return redirect('UserAuth:usersignin')
    return None


# def user_signin(request):

#     if request.method == 'POST':
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('Menu:listmenu')
#         else:
#             messages.error(request, "Invalid username or password")
#     return JsonResponse(request, "signin.html")
def user_signin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user = {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "phone_number": user.phone_number
            }
            return JsonResponse({'status': 'success', 'message': 'Login successful', 'user': user}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password'}, status=401)

    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
    # return JsonResponse({
    #     "message": "Hello from vali!",
    #     "status": "success"
    # })


def logout(request):
    logout(request)
    return redirect('UserAuth:usersignin')

def test_data(request):
    return JsonResponse({
        "message": "Hello from Django!",
        "status": "success"
    })