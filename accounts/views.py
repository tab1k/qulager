from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Profile
from django.views.generic import FormView


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['phone_number']
    template_name = 'accounts/profile/profile_update.html'
    success_url = reverse_lazy('profile_update')

