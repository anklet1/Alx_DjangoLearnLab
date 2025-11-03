# update.md

# Retrieve the book first
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
book.title
# Expected output:
# 'Nineteen Eighty-Four'

