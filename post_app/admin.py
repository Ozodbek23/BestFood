from django.contrib import admin

from post_app.models import Post, PostImage

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'context']
    list_display_links = ['title']
    search_fields = ['title']


class PostImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'image']
    list_display_links = ['post']
    search_fields = ['post']



admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)