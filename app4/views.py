from django.shortcuts import render
from django.views.generic import ListView
from .models import Blogs

# Create your views here.
class HomeView(ListView):
    model = Blogs
    template_name = 'home.html'


class IndexViews(ListView):
    model = Blogs
    template_name = 'index.html'
