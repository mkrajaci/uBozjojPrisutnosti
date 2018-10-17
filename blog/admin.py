from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)       # dodavanje modela u admin panel, u ovom slučaju je to model Post