# Django Book Model - Implementation Summary

## Overview

This project demonstrates proficiency in Django by creating a Book model within the `bookshelf` app, implementing it with specified attributes, and performing CRUD operations using Django's ORM.

## Project Structure

```
LibraryProject/
├── bookshelf/               # Django app
│   ├── models.py           # Book model definition
│   ├── migrations/         # Database migrations
│   └── ...
├── LibraryProject/         # Project settings
│   ├── settings.py         # Added bookshelf to INSTALLED_APPS
│   └── ...
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database
├── create.md               # CREATE operation documentation
├── retrieve.md             # RETRIEVE operation documentation
├── update.md               # UPDATE operation documentation
├── delete.md               # DELETE operation documentation
└── CRUD_operations.md      # Comprehensive CRUD documentation
```

## Implementation Steps Completed

### 1. ✅ Created the bookshelf App

The `bookshelf` app was created using:

```bash
python manage.py startapp bookshelf
```

### 2. ✅ Defined the Book Model

Location: `bookshelf/models.py`

The Book model includes:

- **title**: CharField with max_length=200
- **author**: CharField with max_length=100
- **publication_year**: IntegerField
- ****str**** method for readable representation

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
```

### 3. ✅ Registered App in Settings

Added `'bookshelf'` to `INSTALLED_APPS` in `LibraryProject/settings.py`

### 4. ✅ Created and Applied Migrations

```bash
python manage.py makemigrations bookshelf
python manage.py migrate
```

**Migration Result:**

- Created: `bookshelf/migrations/0001_initial.py`
- Status: ✅ Successfully applied

### 5. ✅ Performed CRUD Operations

All operations were successfully executed in the Django shell:

#### CREATE

```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

**Result:** Created book with ID 1 ✅

#### RETRIEVE

```python
book = Book.objects.get(title="1984")
```

**Result:** Successfully retrieved all attributes ✅

#### UPDATE

```python
book.title = "Nineteen Eighty-Four"
book.save()
```

**Result:** Title updated successfully ✅

#### DELETE

```python
book.delete()
```

**Result:** Book deleted, confirmed with empty QuerySet ✅

### 6. ✅ Documentation Files Created

Individual operation documentation:

- `create.md` - CREATE operation with command and output
- `retrieve.md` - RETRIEVE operation with command and output
- `update.md` - UPDATE operation with command and output
- `delete.md` - DELETE operation with command and output

Comprehensive documentation:

- `CRUD_operations.md` - Complete guide with all operations, outputs, and explanations

## Verification

All operations have been tested and verified:

1. **Model Definition**: ✅ Correctly defined with all required fields
2. **Database Migration**: ✅ Successfully created and applied
3. **CREATE Operation**: ✅ Book created with correct attributes
4. **RETRIEVE Operation**: ✅ Book retrieved and all attributes displayed
5. **UPDATE Operation**: ✅ Title updated from "1984" to "Nineteen Eighty-Four"
6. **DELETE Operation**: ✅ Book deleted and deletion confirmed

## How to Test

To test the CRUD operations yourself:

1. Navigate to the project directory:

   ```bash
   cd LibraryProject
   ```

2. Open the Django shell:

   ```bash
   python manage.py shell
   ```

3. Execute the operations as documented in `CRUD_operations.md`

## Key Learning Outcomes

- ✅ Creating Django apps within a project
- ✅ Defining models with various field types
- ✅ Using Django's migration system
- ✅ Performing CRUD operations using Django ORM
- ✅ Understanding QuerySets and model managers
- ✅ Documenting development processes

## Notes

- The Book model includes a custom `__str__` method for better representation
- All database operations use Django's ORM (no raw SQL)
- The implementation follows Django best practices
- Documentation includes both commands and expected outputs for automated checking
