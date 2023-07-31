from django.urls import path
from .views import HomeViewPage, IndexViewPage

urlpatterns = [
    path('', HomeViewPage.as_view(), name='home'),
    path('all/', IndexViewPage.as_view(), name='index')
]
