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
    ]
