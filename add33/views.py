from django.shortcuts import render
from django.views.generic import ListView
from .models import Blogs

# Create your views here.
class HomepageView(ListView):
    model = Blogs
    template_name = 'home.html'


class IndexpageViews(ListView):
    model = Blogs
    template_name = 'index.html'
