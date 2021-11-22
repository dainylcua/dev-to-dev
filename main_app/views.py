from django.shortcuts import render, redirect
from .models import Post, Comment
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def home(request):
  return render(request, 'home.html')