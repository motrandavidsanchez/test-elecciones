from django.contrib.auth.models import User
from django.db import models

from geodirectory.models import Establishment


class Profile(models.Model):
    dni = models.CharField(max_length=20, blank=True, null=True, verbose_name='DNI')
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
        verbose_name='Usuario',
    )
    establishment = models.ForeignKey(
        Establishment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Establecimiento',
    )

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.establishment.name if self.establishment else '-'
