from django.contrib import admin
from django.utils.timezone import now
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'published_at', 'created_at')  
    list_filter = ('published', 'created_at')  
    search_fields = ('title', 'content', 'author')  
    ordering = ('-created_at',)  
    date_hierarchy = 'published_at'  
    actions = ['publish_posts', 'unpublish_posts']  

    def publish_posts(self, request, queryset):
        queryset.update(published=True, published_at=now())
    publish_posts.short_description = "Pubblica i post selezionati"

    def unpublish_posts(self, request, queryset):
        queryset.update(published=False, published_at=None)
    unpublish_posts.short_description = "Nascondi i post selezionati"