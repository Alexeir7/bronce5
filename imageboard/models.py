from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# here is the userprofile which inherits from the user model of django and adds the profile picture
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    owner = models.ForeignKey(UserProfile, default='')
    title = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='post_images', default='')
    stars = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_on = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    text = models.CharField(max_length=150, default='')
    stars = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
