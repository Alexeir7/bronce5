from django.db import models


# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=50, default='')
    post_image = models.ImageField(upload_to='post_images', default='')
    post_stars = models.IntegerField(default=0)
    post_views = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    comment_text = models.CharField(max_length=150, default='')
    comment_stars = models.IntegerField(default=0)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
