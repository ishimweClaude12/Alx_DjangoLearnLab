"""
Sample queries demonstrating relationships in the relationship_app models.

This script contains query examples for:
1. ForeignKey relationship (Book -> Author)
2. ManyToMany relationship (Library -> Books)
3. OneToOne relationship (Librarian -> Library)
"""

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Query all books by a specific author using ForeignKey relationship.
    
    Args:
        author_name (str): The name of the author
    
    Returns:
        QuerySet: All books written by the specified author
    """
    try:
        # Get the author object
        author = Author.objects.get(name=author_name)
        
        # Query all books by this author using the related_name 'books'
        books = author.books.all()
        
        print(f"Books by {author_name}:")
        for book in books:
            print(f"  - {book.title}")
        
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None


def list_books_in_library(library_name):
    """
    List all books in a library using ManyToMany relationship.
    
    Args:
        library_name (str): The name of the library
    
    Returns:
        QuerySet: All books in the specified library
    """
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        
        # Query all books in this library using the related_name 'books'
        books = library.books.all()
        
        print(f"Books in {library_name}:")
        for book in books:
            print(f"  - {book.title} by {book.author.name}")
        
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library using OneToOne relationship.
    
    Args:
        library_name (str): The name of the library
    
    Returns:
        Librarian: The librarian object for the specified library
    """
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        
        # Access the librarian using the related_name 'librarian'
        librarian = library.librarian
        
        print(f"Librarian for {library_name}: {librarian.name}")
        
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None


# Example usage (can be run from Django shell)
if __name__ == "__main__":
    # These examples assume you have data in your database
    # You can run this script using: python manage.py shell < relationship_app/query_samples.py
    
    print("=" * 50)
    print("Sample Queries for Relationship App")
    print("=" * 50)
    
    # Example 1: Query books by author
    print("\n1. Query books by a specific author:")
    query_books_by_author("J.K. Rowling")
    
    # Example 2: List books in a library
    print("\n2. List all books in a library:")
    list_books_in_library("Central Library")
    
    # Example 3: Retrieve librarian for a library
    print("\n3. Retrieve the librarian for a library:")
    retrieve_librarian_for_library("Central Library")
