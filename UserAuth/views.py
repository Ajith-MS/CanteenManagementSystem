from django.shortcuts import render

# Create your views here.
def user_signUp(request):
    # User = get_user_model()
    # all_user = User.objects.values_list("username", flat=True)
    # all_numbers = CustomUser.objects.values_list("phone_number", flat=True)
    # all_emails = User.objects.values_list("email", flat=True)
    # if request.method == 'POST':
    #     user_name = request.POST.get("username")
    #     first_name = request.POST.get("firstname")
    #     last_name = request.POST.get("lastname")
    #     email = request.POST.get("email")
    #    
    #     phone_number = request.POST.get("phonenumber")
    #     address = request.POST.get("address")
    #  password = request.POST.get("password")
    #     confirm_password = request.POST.get("confirmpassword")

    #     if user_name in all_user:
    #         messages.error(request, "Username already exists!!")
    #     elif email in all_emails:
    #         messages.error(request, "Email already exists!!")
    #     elif phone_number in all_numbers:
    #         messages.error(request, "Phonenumber already exists!!")
    #     elif password != confirm_password:
    #         messages.error(request, "Password and confirm password doesn't match!!")
    #     else:
    #         User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email,password=password, phone_number=phone_number, profile_picture=profile_picture, address=address)
    #         messages.success(request, "Account created successfully")
    #         return redirect('user_authentication:userlogin')
    return render(request, "signUp.html")
