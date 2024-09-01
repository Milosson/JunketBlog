from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Home page for all posts
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Detail view for a single post
]
