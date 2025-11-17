# Delete Operation

## Command

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
```

## Expected Output

```
# The command deletes the book and confirms deletion by retrieving all books
# Output from delete(): (1, {'bookshelf.Book': 1})
# Output from all(): <QuerySet []>
```

## Explanation

This command:

1. Retrieves the book with title "Nineteen Eighty-Four"
2. Deletes the book using the `delete()` method, which returns a tuple with the number of objects deleted
3. Confirms deletion by retrieving all books, which returns an empty QuerySet
