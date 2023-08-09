from django.urls import path
from .views import CustomUserListCreateAPIView,CustomUserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/', CustomUserListCreateAPIView.as_view(),),
    path('api/users/<int:user_id>/', CustomUserRetrieveUpdateDestroyAPIView.as_view(),
         # name='customuser-retrieve-update-destroy'
    ),
]
