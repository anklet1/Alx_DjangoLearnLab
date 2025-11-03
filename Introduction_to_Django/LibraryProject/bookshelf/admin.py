from django.contrib import admin
from .models import Book

# Customize the admin interface for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    search_fields = ('title', 'author')  # Enable search by title or author
    list_filter = ('publication_year',)  # Add filter by publication year

# Register Book with the custom admin settings
admin.site.register(Book, BookAdmin)


# Register your models here.
