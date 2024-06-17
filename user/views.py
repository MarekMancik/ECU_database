from django.shortcuts import render
from django.contrib.auth.forms import *
from .forms import RegistrationForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse


# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # is_validate validation according rules (not right name and psw) return True, of False
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) # OK-return user's instance, NOK-return NOK.
            if user is not None:
                login(request, user)
                return redirect('ecu-tables')
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
