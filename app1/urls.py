from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('add/', DetailPageView.as_view(), name='page')

]
