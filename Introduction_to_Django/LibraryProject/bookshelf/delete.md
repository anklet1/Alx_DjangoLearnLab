# Delete Operation

Command:

```python
from bookshelf.models import Book

book1 = Book.objects.get(title="Nineteen Eighty-Four")
book1.delete()

books = Book.objects.all()
books


Expected Output (example):

(1, {'bookshelf.Book': 1})
<QuerySet []>
