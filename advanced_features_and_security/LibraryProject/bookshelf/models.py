from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom user manager for CustomUser model.
    Handles user creation with additional fields.
    """
    
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        
        if not username:
            raise ValueError('The Username field must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and save a superuser with the given username, email, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    
    Adds additional fields:
    - date_of_birth: Date field for user's birth date
    - profile_photo: Image field for user's profile picture
    """
    
    date_of_birth = models.DateField(
        null=True, 
        blank=True,
        help_text='User date of birth',
        verbose_name='Date of Birth'
    )
    
    profile_photo = models.ImageField(
        upload_to='profile_photos/', 
        blank=True, 
        null=True,
        help_text='User profile photo',
        verbose_name='Profile Photo'
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.username


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
    
    class Meta:
        permissions = [
            ('can_create', 'Can create book'),
            ('can_delete', 'Can delete book'),
        ]
    
    def __str__(self):
        return self.title

