from django.db import models
from stdimage.models import StdImageField


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

