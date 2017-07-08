from django.contrib import admin
from imageboard.models import Post, Comment, UserProfile

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = 'date',

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = 'date',

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile)
