from django.shortcuts import render, redirect
from .models import ROLE_CHOICES, CustomUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from .forms import LoginForm, RegistrationForm


def index(request):
    if request.method == "POST":
        action = request.POST.get('action')  # check what particular button was pressed

        if action == "login":
            login_form = LoginForm(request.POST)
            registration_form = RegistrationForm()
            active_tab = "login"

            if login_form.is_valid():
                user = login_form.user
                login(request, user)
                return redirect('main:index')

        elif action == "registration":
            registration_form = RegistrationForm(request.POST)
            login_form = LoginForm()
            active_tab = "registration"

            if registration_form.is_valid():
                new_user = registration_form.save()
                login(request, new_user)
                return redirect('main:index')

        context = {
            'login_form': login_form,
            'registration_form': registration_form,
            'role_choices': ROLE_CHOICES,
            'active_tab': active_tab,
        }

        return render(request, 'authentication/index.html', context)

    elif request.method == "GET":
        login_form = LoginForm()
        registration_form = RegistrationForm()

        context = {
            'login_form': login_form,
            'registration_form': registration_form,
            'role_choices': ROLE_CHOICES,
            'active_tab': "login",
        }
        return render(request, 'authentication/index.html', context)


def logout_view(request):
    logout(request)  # clean the session up
    return redirect('authentication:index')
