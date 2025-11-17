# Create Operation

## Command

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
```

## Expected Output

```
# The command creates a new Book instance and returns it
# Output: <Book: 1984 by George Orwell (1949)>
```

## Explanation

This command uses Django's ORM to create a new Book instance with:

- title: "1984"
- author: "George Orwell"
- publication_year: 1949

The `create()` method automatically saves the object to the database.
