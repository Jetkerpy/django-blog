from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CreateCommentView,
)


urlpatterns = [
    path('', PostListView.as_view(), name = 'postlar'),
    path('<int:pk>', PostDetailView.as_view(), name = 'detail'),
    path('create/', PostCreateView.as_view(), name = 'create'),
    path('update/<int:pk>/',PostUpdateView.as_view(), name = 'update' ),
    path('delete/<int:pk>/',PostDeleteView.as_view(), name = 'delete' ),
    path('create-comment/<int:pk>/', CreateCommentView.as_view(), name = "create-comment"),




]