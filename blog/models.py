from django.db import models
from django.contrib.auth import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class Post(models.Model):
    title = models.CharField(unique=True, max_length=200)
    image = models.ImageField(upload_to='uploads/%Y/%d/%M', null=False, blank=False)
    description = models.TextField(max_length=4000)
    created_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    category = models.CharField(null=False, blank=False, max_length=200)

    def __str__(self):
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    post_id = models.IntegerField(auto_created=True)

    def __str__(self):
        return self.name



