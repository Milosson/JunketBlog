from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import post_list, post_detail, contact_us, contact_success, comment_edit, create_travel_post

urlpatterns = [
    path('create/', create_travel_post, name='create_travel_post'),
    path('login/', auth_views.LoginView.as_view, name='login'),
    path('', views.post_list, name='home'),  # Home page for all posts
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Detail view for a single post
    path('contact/', contact_us, name='contact_us'),
    path('contact/success/', contact_success, name='contact_success'),
    path('post/<slug:slug>/edit-comment/<int:comment_id>/', comment_edit, name='comment_edit'),  # New URL for editing comments
    path('post/<slug:slug>/delete_comment/<int:comment_id>/',
      views.comment_delete, name='comment_delete')


]
