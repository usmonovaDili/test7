from django.urls import path
from .views import *

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), ),
    path('author/update/<int:pk>/', AuthorUpdateApiView.as_view()),
    path('tags/', TagListCreateView.as_view(), ),
    path('tags/update/<int:pk>/', TagUpdateApiView.as_view()),
    path('posts/', PostListCreateView.as_view(), ),
    path('posts/update/<int:pk>/', PostUpdateApiViews.as_view()),
    path('comments/', CommentListCreateView.as_view(), ),
    path('comments/update/<int:pk>/', CommentUpdateApiView.as_view())
]
