from django.db import models

class Music(models.Model):
    name = models.CharField(max_length=20)
    audio_file = models.CharField(max_length=20)
    durations = models.DurationField()
    info = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

    def __str__(self):
        return self.name

class Selection(models.Model):
    name = models.CharField(max_length=20)
    fk = models.ManyToManyField(Music)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name

