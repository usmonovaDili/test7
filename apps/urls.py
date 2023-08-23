from django.urls import path
from .views import UserGetView

urlpatterns = [
    path('', UserGetView.as_view()),
]
