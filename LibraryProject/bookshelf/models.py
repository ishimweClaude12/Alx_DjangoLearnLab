from django.db import models
from django.conf import settings

# Create your models here.

class Book(models.Model):
    """Book model with user reference using custom user model."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    
    # Reference to custom user model using settings.AUTH_USER_MODEL
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='books_added'
    )
    
    def __str__(self):
        return self.title
