from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from . import forms

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('dashboard2')
        else:
            messages.error(request, "Form is not valid")
    else:
        form = forms.StudentForm()
    return render(request, "dashboard.html", {'form':form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, "Login Successful")
            return redirect('dashboard')
            # return render(request, 'dashboard.html')
        else:
            messages.error(request, "User does not exsist")
    form = AuthenticationForm()
    return render(request, "signin.html", {'form':form})

def signup(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
        else:
            print("form is unvalid")
            messages.error(request, "Input Not Valid")
            return redirect('signup')
        return redirect('singin')
    else:
        form = forms.UserRegisterForm()
    return render(request, "signup.html", {'form1':form})

