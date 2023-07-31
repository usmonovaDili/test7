from django.shortcuts import render
from django.views.generic import ListView
from .models import News


class HomeViewPage(ListView):
    model = News
    template_name = 'home.html'

class IndexViewPage(ListView):
    model = News
    template_name = 'index.html'
