from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Book model.
    Displays title, author, and publication_year in the list view.
    Includes list filters and search capabilities for better usability.
    """
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for these fields in the right sidebar
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality for these fields
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin configuration
admin.site.register(Book, BookAdmin)
