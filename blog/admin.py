from django.contrib import admin
from .models import TravelPost, Tag  # Import the TravelPost and Tag models

class TravelPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'status')  # Display these fields in the list view
    prepopulated_fields = {'slug': ('title',)}  # Automatically fill the slug field based on the title
    list_filter = ('status', 'tags')  # Add filters for status and tags in the sidebar
    search_fields = ('title', 'content')  # Add search functionality for title and content

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name of the tag in the list view

# Register the models with their custom admin classes
admin.site.register(TravelPost, TravelPostAdmin)
admin.site.register(Tag, TagAdmin)

