# Create Operation

Command:

```python
from bookshelf.models import Book

book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book1

Expected Output (example):

<Book: 1984 by George Orwell>


Comment: The Book instance "1984" has been successfully created in the database.
