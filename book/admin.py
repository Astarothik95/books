from django.contrib import admin
from .models import Book, Category, Author, CategoryBook, AuthorBook
from django import forms
from django.forms import formset_factory


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'birth_date', 'death_date', 'wiki_link')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category',)


class CategoryBookAdmin(admin.TabularInline):
    model = CategoryBook
    extra = 1


class AuthorBookAdmin(admin.TabularInline):
    model = AuthorBook
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title_book', 'year', 'desc_book')

    inlines = [
        CategoryBookAdmin, AuthorBookAdmin
    ]
