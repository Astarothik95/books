# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorbook',
            name='author',
        ),
        migrations.RemoveField(
            model_name='authorbook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='categorybook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='categorybook',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, default=0, to='author.Author'),
        ),
        migrations.DeleteModel(
            name='AuthorBook',
        ),
        migrations.DeleteModel(
            name='CategoryBook',
        ),
    ]
