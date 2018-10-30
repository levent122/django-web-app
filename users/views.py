from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


def Register(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():

        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        newUser = User(first_name= first_name, last_name= last_name, username= username, email= email)
        newUser.set_password(password)
        newUser.save()

        login(request, newUser)
        return redirect('index')

    return render(request,'register.html',{'form':form})


def Login(request):

    form = LoginForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        if '@' in username:

            email = User.objects.filter(email= username)

            if email:
                email = email.first().username

                user = authenticate(username= email, password= password)

                if user:

                    login(request,user)
                    messages.success(request,"Wellcome " + str(request.user))
                    return redirect("index")

                else:
                    messages.info(request,"Email or Password is wrong")
                    return redirect("login")

            else:
                messages.info(request,"There is no this account")
                return redirect("login")

        else:

            user = authenticate(username= username, password= password)
            
            if user:
                login(request,user)
                messages.success(request,"Wellcome " + str(request.user))
                return redirect("index")

            else:
                messages.info(request,"Usename or Password is wrong ")
                return redirect("login")


    return render(request,"login.html",{'form':form})


def Logout(request):
    logout(request)
    return redirect('index')

