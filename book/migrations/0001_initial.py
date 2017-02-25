# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('surname', models.CharField(verbose_name='Фамилия', max_length=45)),
                ('name', models.CharField(verbose_name='Имя', max_length=35)),
                ('patronymic', models.CharField(verbose_name='Отчество', max_length=50, blank=True)),
                ('image', stdimage.models.StdImageField(verbose_name='Изображение', blank=True, upload_to='img/authors')),
                ('birth_date', models.DateField(verbose_name='Дата рождения', blank=True, null=True)),
                ('death_date', models.DateField(verbose_name='Дата смерти', blank=True, null=True)),
                ('wiki_link', models.URLField(verbose_name='Wikipedia', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('author', models.ForeignKey(to='book.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title_book', models.CharField(verbose_name='Название книги', max_length=250)),
                ('desc_book', models.TextField(verbose_name='Краткое описание', max_length=255)),
                ('year', models.IntegerField(verbose_name='Год издания', blank=True, default=2017)),
                ('image', stdimage.models.StdImageField(verbose_name='Изображение', blank=True, upload_to='img/books')),
                ('wiki_link', models.URLField(verbose_name='Wikipedia', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name_category', models.CharField(verbose_name='Название категории', max_length=25)),
                ('desc_category', models.CharField(verbose_name='Описание категории', max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('book', models.ForeignKey(to='book.Book')),
                ('category', models.ForeignKey(to='book.Category')),
            ],
        ),
        migrations.AddField(
            model_name='authorbook',
            name='book',
            field=models.ForeignKey(to='book.Book'),
        ),
    ]
