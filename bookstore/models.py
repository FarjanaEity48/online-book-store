from django.db import models

# Create your models here.


class Book(models.Model):
    book_title = models.CharField(max_length=100)
    book_desc = models.TextField(max_length=1000)
    book_pic = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_title
