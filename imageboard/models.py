from django.db import models


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=150, default=0)
    email = models.EmailField(default='')
    picture = models.ImageField(upload_to='profile_images', default='')


class Post(models.Model):
    id = models.ForeignKey(UserProfile, default='')
    title = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='post_images', default='')
    stars = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    id = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    text = models.CharField(max_length=150, default='')
    stars = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
