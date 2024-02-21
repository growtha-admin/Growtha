from django.contrib import admin
from .models import BlogPost, Author, Tag



admin.site.site_header = 'Growtha Administration'

admin.site.site_title = 'Growtha'


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'url_hash', 'author', 'is_featured',)
    
    list_filter = ('published_at', 'is_featured',)

admin.site.register(BlogPost, BlogPostAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'joined_at', 'author_hash')
    
    list_filter = ('joined_at',)

admin.site.register(Author, AuthorAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'tag_hash',)

admin.site.register(Tag, TagAdmin)

    
