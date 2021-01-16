from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', default=18, null=True)

    activation_key = models.CharField(verbose_name='Ключ подтверждения',max_length=128, blank=True, null=True)
    activation_key_expires = models.DateTimeField(verbose_name='Актуальность ключа',default=(now() + timedelta(hours=48)))

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def is_activation_key_expired(self):
        if now() < self.activation_key_expires:
            return False
        return True

    def __str__(self):
        return self.username
