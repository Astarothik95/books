from django.contrib import admin
from .models import Book, Category, CategoryBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title_book', 'author', 'year', 'desc_book')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category',)


@admin.register(CategoryBook)
class CategoryBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'category')

