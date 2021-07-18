# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Book(models.Model):
    user_borrowed = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=80)

    def borrow_book(self, user):
        if self.user_borrowed is not None:
            return False
        self.user_borrowed = user
        self.save()

    def return_book(self):
        self.user_borrowed = None
        self.save()
    def __str__(self):
        return self.name

