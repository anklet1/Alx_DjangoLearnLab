# Retrieve Operation

Command:

```python
from bookshelf.models import Book

books = Book.objects.all()
books

Expected Output (example):

<QuerySet [<Book: 1984 by George Orwell>]>


Comment: All Book instances are retrieved from the database, displaying the "1984" book created earlier.
