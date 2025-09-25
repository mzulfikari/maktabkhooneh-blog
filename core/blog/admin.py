from django.contrib import admin
from .models import Category,Post

class PostsAdmin(admin.ModelAdmin):
    list_display= [
        'author','title','status','created_date','publish_date'
    ]

admin.site.register(Post)
admin.site.register(Category)