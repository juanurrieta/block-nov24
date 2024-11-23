from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    

admin.site.register(Post, PostAdmin)