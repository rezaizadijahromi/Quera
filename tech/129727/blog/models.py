
from django.utils import timezone
from django.db import models
from account.models import User

STATUS_CHOICES = (
    ("d", "draft"),
    ("p", "publish ")
)


class Category(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class Article(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, default="", blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=False)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default="d")

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.author)
