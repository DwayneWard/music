from django.db import models

# class Music(models.Model):
#     name = models.CharField(max_length=20)
#     audio_file = models.CharField(max_length=20)
#     durations = models.DurationField()
#     info = models.TextField(max_length=200)
#
#     class Meta:
#         verbose_name = 'Трек'
#         verbose_name_plural = 'Треки'
#
#     def __str__(self):
#         return self.name
#
#
# class Selection(models.Model):
#     name = models.CharField(max_length=20)
#     fk = models.ManyToManyField(Music)
#
#     class Meta:
#         verbose_name = 'Подборка'
#         verbose_name_plural = 'Подборки'
#
#     def __str__(self):
#         return self.name
#
#
# class FavoriteMusic(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     music = models.ManyToManyField(Music, verbose_name="list of music for user")
#
#     class Meta:
#         verbose_name = 'Избранное'
#         verbose_name_plural = 'Избранное'
#
#     def __str__(self):
#         return self.name
#
from user.models import User


class Track(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    release_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=50)
    duration_in_seconds = models.IntegerField()
    album = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True)
    stared_user = models.ManyToManyField(User, related_name='favorite_tracks')

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Track)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name
