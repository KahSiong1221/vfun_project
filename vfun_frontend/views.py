from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View

import requests

from vfun_project import settings
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm


def sportshall_list(request):
    response = requests.get('http://127.0.0.1:8000/api-v1/sportshalls/')
    sportshalls = response.json()
    return render(request, 'vfun_frontend/sportshalls.html', {'sportshalls': sportshalls})


def my_sportshall_list(request):
    headers = {'Authorization': settings.AUTH_TOKEN}
    response = requests.get('http://127.0.0.1:8000/api-v1/mysportshalls/', headers=headers)
    sportshalls = response.json()
    return render(request, 'vfun_frontend/sportshall_manage.html', {'sportshalls': sportshalls})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'vfun_frontend/password_reset.html'
    email_template_name = 'vfun_frontend/password_reset_email.html'
    subject_template_name = 'vfun_frontend/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'vfun_frontend/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'vfun_frontend/profile.html', {'user_form': user_form, 'profile_form': profile_form})


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'vfun_frontend/register.html'

    def get(self, request, *args, **kwargs):
        # create a new instance of an empty form
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        # create a new instance of the form with post data
        form = self.form_class(request.POST)

        if form.is_valid():
            # save user to database
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)
