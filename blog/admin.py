from django.contrib import admin
from .models import TravelPost, Tag  # Import the TravelPost and Tag models


admin.site.register(TravelPost)
admin.site.register(Tag)