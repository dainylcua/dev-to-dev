from django.contrib import admin
from .models import Topic, Comment, Post

# Register your models here.
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Post)