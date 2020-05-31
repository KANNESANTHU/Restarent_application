from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    image=models.ImageField(upload_to='blog/',blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    categery=models.ForeignKey('Categery',on_delete=models.SET_NULL,null=True)
    created=models.DateTimeField(default=timezone.now)
    tags = TaggableManager(blank=True)


    def __str__(self):
        return self.title


class Categery(models.Model):
    categery_name=models.CharField(max_length=50)

    class Meta:
        verbose_name='categery'
        verbose_name_plural='categeries'

    def __str__(self):
        return self.categery_name

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    content=models.TextField()
    created=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.content)
# Create your models here.
