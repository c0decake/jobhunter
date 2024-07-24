from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginUserForm, RegisterUserForm


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user:
                request.session['user_id'] = user.id
                login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = LoginUserForm()
    return render(request, 'Auth/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth:login'))


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = RegisterUserForm()
    return render(request, 'Auth/registration.html', {'form': form})
