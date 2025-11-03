
---

**`update.md`**  

```markdown
# Update Operation

Command:

```python
from bookshelf.models import Book

book1 = Book.objects.get(title="1984")
book1.title = "Nineteen Eighty-Four"
book1.save()
book1

Expected Output (example):

<Book: Nineteen Eighty-Four by George Orwell>


Comment: The title of the book has been updated from "1984" to "Nineteen Eighty-Four".
