"""
Sample queries demonstrating ForeignKey, ManyToMany, and OneToOne relationships.

This script contains queries to:
1. Query all books by a specific author (ForeignKey relationship)
2. List all books in a library (ManyToMany relationship)
3. Retrieve the librarian for a library (OneToOne relationship)
"""

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    
    This demonstrates the ForeignKey relationship from Book to Author.
    We can access books through the related_name 'books' on the Author model.
    
    Args:
        author_name (str): The name of the author to search for.
    
    Returns:
        QuerySet: All books by the specified author.
    """
    try:
        # Get the author by name
        author = Author.objects.get(name=author_name)
        
        # Query all books by this author using objects.filter
        books = Book.objects.filter(author=author)
        
        print(f"\nBooks by {author_name}:")
        for book in books:
            print(f"  - {book.title}")
        
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None


def list_books_in_library(library_name):
    """
    List all books in a library.
    
    This demonstrates the ManyToMany relationship between Library and Book.
    We access books through the ManyToManyField 'books' on the Library model.
    
    Args:
        library_name (str): The name of the library to search for.
    
    Returns:
        QuerySet: All books in the specified library.
    """
    try:
        # Get the library by name
        library = Library.objects.get(name=library_name)
        
        # List all books in this library
        books = library.books.all()
        
        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f"  - {book.title} by {book.author.name}")
        
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    
    This demonstrates the OneToOne relationship from Librarian to Library.
    We can access the librarian through the related_name 'librarian' on the Library model.
    
    Args:
        library_name (str): The name of the library to search for.
    
    Returns:
        Librarian: The librarian associated with the specified library.
    """
    try:
        # Get the library by name
        library = Library.objects.get(name=library_name)
        
        # Retrieve the librarian for this library using the related_name 'librarian'
        librarian = library.librarian
        
        print(f"\nLibrarian for {library_name}:")
        print(f"  - {librarian.name}")
        
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None


# Example usage (commented out - uncomment to run):
# if __name__ == "__main__":
#     # Make sure you have created some sample data first:
#     # - Authors and Books
#     # - Libraries with books
#     # - Librarians assigned to libraries
#     
#     # Query all books by a specific author
#     query_books_by_author("J.K. Rowling")
#     
#     # List all books in a library
#     list_books_in_library("Central Library")
#     
#     # Retrieve the librarian for a library
#     retrieve_librarian_for_library("Central Library")
