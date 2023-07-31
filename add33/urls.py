from  django.urls import path
from .views import HomepageView,IndexpageViews

urlpatterns=[
    path('',HomepageView.as_view(),name='home'),
    path('add/',IndexpageViews.as_view(),name='index')
]