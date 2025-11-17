# CRUD Operations Documentation

This document provides a comprehensive guide to the CRUD (Create, Retrieve, Update, Delete) operations performed on the Book model using Django's ORM through the Django shell.

## Setup

First, open the Django shell:

```bash
python manage.py shell
```

## 1. CREATE Operation

### Command:

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
```

### Output:

```
<Book: 1984 by George Orwell (1949)>
```

### Explanation:

The `create()` method creates a new Book instance with the specified attributes and automatically saves it to the database. The return value is the newly created Book object.

---

## 2. RETRIEVE Operation

### Command:

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

### Output:

```
Title: 1984
Author: George Orwell
Publication Year: 1949
```

### Explanation:

The `get()` method retrieves a single Book instance that matches the specified criteria. We then access and display all the attributes of the retrieved book object.

---

## 3. UPDATE Operation

### Command:

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
```

### Output:

```
<Book: Nineteen Eighty-Four by George Orwell (1949)>
```

### Explanation:

To update a record:

1. First, retrieve the object using `get()`
2. Modify the desired field(s)
3. Call `save()` to persist the changes to the database
   The updated object is returned showing the new title.

---

## 4. DELETE Operation

### Command:

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
```

### Output:

```
(1, {'bookshelf.Book': 1})
<QuerySet []>
```

### Explanation:

The `delete()` method removes the object from the database and returns a tuple containing:

- The number of objects deleted (1)
- A dictionary with the breakdown of deletions by model

Confirming with `Book.objects.all()` returns an empty QuerySet, proving the book was successfully deleted.

---

## Additional Notes

### Other Useful Query Methods:

- `Book.objects.all()` - Retrieves all books
- `Book.objects.filter(author="George Orwell")` - Retrieves all books by a specific author
- `Book.objects.count()` - Returns the total number of books
- `Book.objects.first()` - Returns the first book
- `Book.objects.last()` - Returns the last book

### Best Practices:

1. Always import the model before performing operations
2. Use `get()` when you expect a single result
3. Use `filter()` when you expect multiple results
4. Always call `save()` after modifying an object to persist changes
5. Use `create()` for creating and saving in one step, or use `save()` after instantiating a new object
