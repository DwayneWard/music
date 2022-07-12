from django.db import models
from django.urls import reverse

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
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('track', kwargs={'track_slug': self.slug} )



class Selection(models.Model):
    name = models.CharField(max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Track)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name
