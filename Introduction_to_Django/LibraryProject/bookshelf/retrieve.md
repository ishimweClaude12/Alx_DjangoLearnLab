# Retrieve Operation

## Command

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

## Expected Output

```
# The command retrieves the book with title "1984" and displays all its attributes
# Output:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
```

## Explanation

This command uses the `get()` method to retrieve a single Book instance that matches the specified criteria (title="1984"). It then prints all the attributes of the book.
