import calendar
from datetime import datetime, timedelta

import jwt
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from config import settings


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=2)

        return jwt.encode({
            'id': self.pk,
            'exp': calendar.timegm(dt.timetuple())
        }, settings.SECRET_KEY, algorithm='HS256')

    def __str__(self):
        return self.username
