from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_author', 'post_content', 'published_date')
    search_fields = ('post_title', 'post_author')
    list_filter = ('published_date',)