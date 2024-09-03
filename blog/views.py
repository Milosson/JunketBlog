from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import TravelPost, Comment
from .forms import CommentForm


def post_detail(request, slug):
    post = get_object_or_404(TravelPost, slug=slug)  # Retrieve the TravelPost by slug
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    # Automatically approve comments that meet the condition
    for comment in comments:
        if comment.is_auto_approved() and not comment.approved:
            comment.approved = True
            comment.save()

    return render(
        request, 
        'blog/post_detail.html', 
        {
            'post': post,
            'comments': comments,
            'comment_count': comment_count,
            'comment_form': comment_form,
            
            },
        )  

def post_list(request):
    posts = TravelPost.objects.filter(status=1).order_by('-created_on')  # Fetch all TravelPost objects
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'posts': page_obj.object_list, 'is_paginated': page_obj.has_other_pages(), 'page_obj': page_obj})