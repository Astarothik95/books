# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20170224_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('book', models.ForeignKey(to='book.Book')),
                ('category', models.ForeignKey(to='book.Category')),
            ],
        ),
    ]
