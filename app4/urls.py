from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', IndexViews.as_view(), name='index')
]
