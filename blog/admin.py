from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','category' ,'status']
    list_filter = ['status', 'author']
    search_fields = ['title', 'author', 'category']
    prepopulated_fields = {"slug":("title",)}
    raw_id_fields = ["author"]

admin.site.register(Post, PostAdmin)