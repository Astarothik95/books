# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title_book', models.CharField(verbose_name='Название книги', max_length=250)),
                ('desc_book', models.TextField(verbose_name='Краткое описание', max_length=255)),
                ('year', models.IntegerField(verbose_name='Год издания', blank=True, default=2017)),
                ('image', stdimage.models.StdImageField(verbose_name='Изображение', blank=True, upload_to='img/books')),
                ('wiki_link', models.URLField(verbose_name='Wikipedia', blank=True)),
                ('author', models.ForeignKey(null=True, default=0, to='author.Author')),
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
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, default=0, to='book.Category'),
        ),
    ]
