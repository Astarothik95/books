from django.db import models
from stdimage.models import StdImageField
from author.models import Author
import datetime


class Book(models.Model):
    title_book = models.CharField('Название книги', max_length=250)
    desc_book = models.TextField('Краткое описание', max_length=255)
    author = models.ForeignKey('author.Author', null=True, default=0)
    category = models.ForeignKey('Category', null=True, default=0, blank=True)
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
    book = models.ForeignKey('Book')
    category = models.ForeignKey('Category')

    def add(self):
        self.save()
