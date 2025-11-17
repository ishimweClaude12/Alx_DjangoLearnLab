from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
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


# Authentication Views

def register(request):
    """
    User registration view.
    Handles user registration using Django's UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def user_login(request):
    """
    User login view.
    Handles user authentication and login.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_books')
    return render(request, 'relationship_app/login.html')


def user_logout(request):
    """
    User logout view.
    Logs out the current user and displays logout confirmation.
    """
    logout(request)
    return render(request, 'relationship_app/logout.html')


# Role-Based Access Control Views

def is_admin(user):
    """Check if user has Admin role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    """Check if user has Librarian role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    """Check if user has Member role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    """
    Admin view - accessible only to users with Admin role.
    """
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    """
    Librarian view - accessible only to users with Librarian role.
    """
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    """
    Member view - accessible only to users with Member role.
    """
    return render(request, 'relationship_app/member_view.html')


# Permission-Based Views for Book Operations

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """
    Add a new book - requires can_add_book permission.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        if title and author_id:
            from .models import Author
            try:
                author = Author.objects.get(id=author_id)
                Book.objects.create(title=title, author=author)
                return redirect('list_books')
            except Author.DoesNotExist:
                pass
    
    from .models import Author
    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    """
    Edit an existing book - requires can_change_book permission.
    """
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('list_books')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        if title and author_id:
            from .models import Author
            try:
                author = Author.objects.get(id=author_id)
                book.title = title
                book.author = author
                book.save()
                return redirect('list_books')
            except Author.DoesNotExist:
                pass
    
    from .models import Author
    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    """
    Delete a book - requires can_delete_book permission.
    """
    try:
        book = Book.objects.get(id=book_id)
        if request.method == 'POST':
            book.delete()
            return redirect('list_books')
        return render(request, 'relationship_app/delete_book.html', {'book': book})
    except Book.DoesNotExist:
        return redirect('list_books')




