from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    Category_choice=(
        ("Programming", "Programming"),
        ("Technical", "Technical"),
        ("Fashion", "Fashion"),
        ("Life style", "Life style"),
        ("History", "History"),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.CharField(max_length=100, )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    