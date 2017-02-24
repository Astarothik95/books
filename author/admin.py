from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'birth_date', 'death_date', 'wiki_link')

