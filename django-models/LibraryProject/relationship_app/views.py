from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Book
from .models import Library

# Create your views here.


def list_books(request):
    """
    Function-based view to list all books.
    Displays all books with their titles and authors.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    """
    Class-based view to display details of a specific library.
    Shows the library name and all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

