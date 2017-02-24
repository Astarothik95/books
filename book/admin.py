from django.contrib import admin
from .models import Book, Category
from author.models import Author


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title_book', 'year', 'desc_book')
    suit_form_includes = (
        'Author.author', 'category',
    )
