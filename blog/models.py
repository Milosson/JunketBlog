from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Status choices for TravelPost
STATUS_CHOICES = (
    (0, "Draft"),      # Indicates the post is a draft
    (1, "Published"),  # Indicates the post has been published
)

class TravelPost(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Title of the travel post
    slug = models.SlugField(max_length=200, unique=True)  # Slug for a URL-friendly representation
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name="travel_posts"  # Author of the post
    ) 
    content = models.TextField()  # Main content of the travel post
    created_on = models.DateTimeField(auto_now_add=True)  # Timestamp for when the post was created
    updated_on = models.DateTimeField(auto_now=True)  # Timestamp for the last update of the post
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)  # Status of the post (draft or published)
    excerpt = models.TextField(blank=True)  # Short summary of the post
    location = models.CharField(max_length=100)  # Location related to the travel post
    travel_date = models.DateField()  # Date of the travel
    tags = models.ManyToManyField('Tag', blank=True)  # Tags to categorize the travel post

    class Meta:
        ordering = ['-created_on']  # Order posts by creation date, newest first

    def __str__(self):
        return f"{self.title} | written by {self.author}"  # Return the title as the string representation of the post

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)  # Unique name for the tag

    def __str__(self):
        return self.name  # Return the name of the tag as its string representation


class Comment(models.Model):
    post = models.ForeignKey(
        TravelPost, on_delete=models.CASCADE, related_name="comments")  # Linking the TravelPost
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")  # Linking to User
    body = models.TextField()  # Text content of the comment
    approved = models.BooleanField(default=False)  # Approval status
    created_on = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    tags = models.ManyToManyField(Tag, blank=True, related_name="comment_tags")  # Optional tagging!

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

    def is_auto_approved(self):
        # Auto-approve comments that are created within the last hour
        # Check if created_on is None first
        if self.created_on is None:
            return False
        return self.created_on <= timezone.now() - timedelta(hours=1)  # Changed to check for last hour

    def save(self, *args, **kwargs):
        if self.is_auto_approved():
            self.approved = True  # Automatically approve if the condition is met
        super().save(*args, **kwargs)  # Call the original save method


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Contact Request from {self.name}'