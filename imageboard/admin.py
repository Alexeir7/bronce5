from django.contrib import admin
from imageboard.models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = 'post_date',

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = 'comment_date',

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
