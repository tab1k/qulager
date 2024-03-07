from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Advertisement


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisements/advertisement_list.html'


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    fields = ['title', 'description', 'price']  # добавьте другие поля объявления при необходимости
    template_name = 'advertisements/advertisement_form.html'
    success_url = reverse_lazy('advertisement_list')


class AdvertisementUpdateView(LoginRequiredMixin, UpdateView):
    model = Advertisement
    fields = ['title', 'description', 'price']  # добавьте другие поля объявления при необходимости
    template_name = 'advertisements/advertisement_form.html'
    success_url = reverse_lazy('advertisement_list')


class AdvertisementDeleteView(LoginRequiredMixin, DeleteView):
    model = Advertisement
    template_name = 'advertisements/advertisement_confirm_delete.html'
    success_url = reverse_lazy('advertisement_list')


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisements/advertisement_detail.html'
