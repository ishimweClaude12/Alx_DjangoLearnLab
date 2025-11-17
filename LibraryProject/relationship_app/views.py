from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
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



