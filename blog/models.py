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
    Status_choice=(
        ("Draft", "Draft"),
        ('published', 'published')
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.CharField(max_length=100, choices=Category_choice)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    status = models.CharField(max_length=100, choices=Status_choice, default="Draft")
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    