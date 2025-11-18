# LibraryProject - Django Security and Permissions

## Overview

This Django project implements a custom user model with enhanced security features and a permission-based access control system for managing books.

## Features

### Custom User Model

- Extended `AbstractUser` with additional fields:
  - `date_of_birth`: Optional date field for user's birth date
  - `profile_photo`: Optional image field for profile pictures
- Custom user manager (`CustomUserManager`) for user creation
- Configured as `AUTH_USER_MODEL` in settings

### Permissions System

The Book model includes custom permissions:

- `can_create`: Permission to create books
- `can_delete`: Permission to delete books

### Views with Permission Protection

- `book_list`: View to list all books (requires `can_create` permission)
- Uses `@permission_required` decorator with `raise_exception=True`

## Setup Instructions

### 1. Install Dependencies

```bash
pip install django pillow
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser

```bash
python manage.py createsuperuser
```

### 4. Run Development Server

```bash
python manage.py runserver
```

## Usage

### Assigning Permissions

1. Access Django Admin at `http://localhost:8000/admin/`
2. Navigate to Users
3. Select a user and assign the following permissions:
   - `bookshelf | book | Can create book`
   - `bookshelf | book | Can delete book`

### Accessing Views

- Users without proper permissions will receive a 403 Forbidden error when attempting to access protected views
- The `book_list` view requires the `can_create` permission

## Project Structure

```
LibraryProject/
├── bookshelf/              # Main app
│   ├── models.py          # CustomUser and Book models
│   ├── views.py           # Permission-protected views
│   ├── admin.py           # Custom admin configuration
│   └── migrations/        # Database migrations
├── LibraryProject/        # Project settings
│   ├── settings.py        # Configuration (AUTH_USER_MODEL)
│   └── urls.py            # URL routing
└── manage.py              # Django management script
```

## Security Features

- Custom user authentication system
- Permission-based access control
- Protected views with `@permission_required` decorator
- Exception raising for unauthorized access (`raise_exception=True`)

## Models

### CustomUser

Extends Django's `AbstractUser` with:

- `date_of_birth` (DateField, optional)
- `profile_photo` (ImageField, optional)

### Book

- `title` (CharField)
- `author` (CharField)
- `publication_year` (IntegerField)
- `added_by` (ForeignKey to CustomUser)
- Custom permissions: `can_create`, `can_delete`
