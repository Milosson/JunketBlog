from django.contrib import admin
from .models import TravelPost, Tag, Comment
from django_summernote.admin import SummernoteModelAdmin

# Custom admin class for TravelPost
@admin.register(TravelPost)
class TravelPostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')  # Added created_on to display
    search_fields = ['title', 'content']  # Allow searching by title and content
    list_filter = ('status', 'tags')  # Filter by status and tags
    prepopulated_fields = {'slug': ('title',)}  # Auto-populate slug
    summernote_fields = ('content',)  # Enable rich text editing for content
    ordering = ('-created_on',)  # Order posts by created_on date

# Admin class for Tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display tag name

# Admin class for Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_on', 'approved')  # Adjust fields as necessary
    list_filter = ('approved',)
    search_fields = ('author', 'content')  # Allow searching by author and content
