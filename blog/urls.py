from django.urls import path
from . import views
from .views import post_list, post_detail, contact_us, contact_success, comment_edit

urlpatterns = [
    path('', views.post_list, name='home'),  # Home page for all posts
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Detail view for a single post
    path('contact/', contact_us, name='contact_us'),
    path('contact/success/', contact_success, name='contact_success'),
    path('post/<slug:slug>/edit-comment/<int:comment_id>/', comment_edit, name='comment_edit'),  # New URL for editing comments
]
