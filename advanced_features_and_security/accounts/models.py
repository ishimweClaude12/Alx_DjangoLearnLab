from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom user manager for CustomUser model.
    Handles user creation with additional fields.
    """
    
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given username, email, and password.
        
        Args:
            username (str): The username for the user
            email (str): The email address for the user
            password (str): The password for the user
            **extra_fields: Additional fields like date_of_birth, profile_photo, etc.
        
        Returns:
            CustomUser: The created user instance
        
        Raises:
            ValueError: If email is not provided
        """
        if not email:
            raise ValueError('The Email field must be set')
        
        if not username:
            raise ValueError('The Username field must be set')
        
        # Normalize the email address
        email = self.normalize_email(email)
        
        # Create user instance
        user = self.model(username=username, email=email, **extra_fields)
        
        # Set password (hashed)
        user.set_password(password)
        
        # Save to database
        user.save(using=self._db)
        
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and save a superuser with the given username, email, and password.
        
        Args:
            username (str): The username for the superuser
            email (str): The email address for the superuser
            password (str): The password for the superuser
            **extra_fields: Additional fields
        
        Returns:
            CustomUser: The created superuser instance
        """
        # Set default values for superuser flags
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        # Validate superuser flags
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
    
    Uses CustomUserManager for user creation and management.
    """
    
    # Additional custom fields
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

    # Assign custom manager
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']

    def __str__(self):
        """String representation of the user."""
        return self.username
    
    def get_full_name(self):
        """Return the user's full name."""
        return f"{self.first_name} {self.last_name}".strip() or self.username
    
    def get_age(self):
        """Calculate and return the user's age if date_of_birth is set."""
        if self.date_of_birth:
            from datetime import date
            today = date.today()
            age = today.year - self.date_of_birth.year
            # Adjust if birthday hasn't occurred this year
            if today.month < self.date_of_birth.month or \
               (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
                age -= 1
            return age
        return None
