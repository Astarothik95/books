from django.db import models
from stdimage.models import StdImageField
import datetime


class Author(models.Model):
    surname = models.CharField('Фамилия', max_length=45)
    name = models.CharField('Имя', max_length=35)
    patronymic = models.CharField('Отчество', blank=True, max_length=50)
    image = StdImageField('Изображение', upload_to='img/authors', blank=True)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    death_date = models.DateField('Дата смерти', null=True, blank=True)
    wiki_link = models.URLField('Wikipedia', blank=True)

    def add(self):
        self.save()

    def __str__(self):
        return str(self.surname)


class Book(models.Model):
    title_book = models.CharField('Название книги', max_length=250)
    desc_book = models.TextField('Краткое описание', max_length=255)
    year = models.IntegerField(
        'Год издания',
        blank=True,
        default=datetime.datetime.now().year
    )
    image = StdImageField('Изображение', upload_to='img/books', blank=True)
    wiki_link = models.URLField('Wikipedia', blank=True)

    def add(self):
        self.save()

    def __str__(self):
        return str(self.title_book)


class Category(models.Model):
    name_category = models.CharField('Название категории', max_length=25)
    desc_category = models.CharField('Описание категории', max_length=100, blank=True)

    def add(self):
        self.save()

    def __str__(self):
        return str(self.name_category)


class CategoryBook(models.Model):
    category = models.ForeignKey('Category')
    book = models.ForeignKey('Book')

    def add(self):
        self.save()


class AuthorBook(models.Model):
    author = models.ForeignKey('Author')
    book = models.ForeignKey('Book')

    def add(self):
        self.save()

