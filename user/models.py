from django.db import models

from music.models import Music


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name


class FavoriteMusic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ManyToManyField(Music, verbose_name="list of music for user")

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return self.name