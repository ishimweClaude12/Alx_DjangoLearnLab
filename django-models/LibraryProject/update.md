# Update Operation

## Command

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
```

## Expected Output

```
# The command updates the title of the book from "1984" to "Nineteen Eighty-Four"
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
```

## Explanation

This command:

1. Retrieves the book with title "1984"
2. Updates the title field to "Nineteen Eighty-Four"
3. Saves the changes to the database using the `save()` method
4. Returns the updated book instance
