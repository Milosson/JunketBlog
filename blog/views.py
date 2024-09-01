from django.shortcuts import render, get_object_or_404
from .models import TravelPost

def post_detail(request, slug):
    post = get_object_or_404(TravelPost, slug=slug)  # Retrieve the TravelPost by slug
    return render(request, 'blog/post_detail.html', {'post': post})  # Render the detail template


def post_list(request):
    posts = TravelPost.objects.filter(status=1).order_by('-created_on')  # Fetch all TravelPost objects
    return render(request, 'blog/travelpost_list.html', {'posts': posts})  # Render the list template