from django.shortcuts import render
from django.contrib.auth.forms import *
from .forms import RegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import login


# Create your views here.
def sing_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
