from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import TravelPost, Comment
from .forms import CommentForm
from .forms import ContactForm

def post_detail(request, slug):
    post = get_object_or_404(TravelPost, slug=slug)  # Retrieve the TravelPost by slug
    comments = post.comments.all().order_by("-created_on")
    comment_count = comments.filter(approved=True).count()
    comment_form = CommentForm()

    # Handle comment submission
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()  # Save the comment, which may auto-approve
            messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )
            return redirect('post_detail', slug=post.slug)

    # Manually approve comments that meet the condition
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

    return render(request, 'blog/index.html', {
        'posts': page_obj.object_list, 
        'is_paginated': page_obj.has_other_pages(), 
        'page_obj': page_obj,
    })

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a success page
        else: 
            messages.error(request, "There was an error with your submission, Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
