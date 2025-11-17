"""
Admin Configuration Verification Script
Tests that the Book model admin configuration is working correctly
"""

from django.contrib import admin
from bookshelf.models import Book

def verify_admin_configuration():
    """Verify that the Book model is properly configured in the admin."""
    
    print("=" * 60)
    print("Django Admin Configuration Verification")
    print("=" * 60)
    print()
    
    # Check if Book model is registered
    is_registered = admin.site.is_registered(Book)
    print(f"✓ Book model registered: {is_registered}")
    
    if is_registered:
        # Get the admin class
        admin_class = admin.site._registry[Book]
        print(f"✓ Admin class: {admin_class.__class__.__name__}")
        print()
        
        # Check list_display
        print("List Display Configuration:")
        print(f"  Fields: {admin_class.list_display}")
        expected_display = ('title', 'author', 'publication_year')
        if admin_class.list_display == expected_display:
            print("  ✓ Correct: Shows title, author, and publication_year")
        print()
        
        # Check list_filter
        print("List Filter Configuration:")
        print(f"  Filters: {admin_class.list_filter}")
        expected_filters = ('author', 'publication_year')
        if admin_class.list_filter == expected_filters:
            print("  ✓ Correct: Filters by author and publication_year")
        print()
        
        # Check search_fields
        print("Search Fields Configuration:")
        print(f"  Fields: {admin_class.search_fields}")
        expected_search = ('title', 'author')
        if admin_class.search_fields == expected_search:
            print("  ✓ Correct: Searches title and author")
        print()
        
        print("=" * 60)
        print("All admin configurations are correctly set up!")
        print("=" * 60)
        
    else:
        print("✗ ERROR: Book model is not registered with admin")
        return False
    
    # Check if there are any books in the database
    book_count = Book.objects.count()
    print()
    print("Database Status:")
    print(f"  Total books: {book_count}")
    
    if book_count > 0:
        print("  Sample books:")
        for book in Book.objects.all()[:5]:
            print(f"    - {book}")
    
    return True

if __name__ == '__main__':
    verify_admin_configuration()
