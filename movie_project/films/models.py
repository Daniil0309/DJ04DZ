from django.db import models

class Film(models.Model):
    title = models.CharField('Название фильма',max_length=100)
    description = models.TextField('Описание')
    review = models.TextField('Обзор')

    def __str__(self):
        return self.title
