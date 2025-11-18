from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.

@permission_required('bookshelf.can_create', raise_exception=True)
def book_list(request):
    """
    View to list all books.
    Requires can_create permission.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
