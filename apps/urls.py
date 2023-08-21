from django.urls import path
from .views import ListCreateUserView, RetrieveUpdateDestroyUserView

urlpatterns = [
    path('', ListCreateUserView.as_view()),
    path('refresh/<int:pk>/', RetrieveUpdateDestroyUserView.as_view()),
]

