from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messaging/message_list.html'


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['recipient', 'content']  # добавьте другие поля сообщения при необходимости
    template_name = 'messaging/message_form.html'
    success_url = reverse_lazy('message_list')

