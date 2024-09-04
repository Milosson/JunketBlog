from django.urls import path
from . import views
from .views import contact_us, contact_success

urlpatterns = [
    path('', views.post_list, name='home'),  # Home page for all posts
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Detail view for a single post
    path('contact/', contact_us, name='contact_us'),
    path('contact/success/', contact_success, name='contact_success'),
]
