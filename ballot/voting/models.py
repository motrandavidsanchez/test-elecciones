from django.db import models

from geodirectory.models import Table


class Voter(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    dni = models.PositiveIntegerField(unique=True, verbose_name='DNI')
    birth_date = models.DateField(verbose_name='Fecha de nacimiento')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Mesa'
    )
    has_voted = models.BooleanField(default=False, verbose_name='Votó')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Voter'
        verbose_name_plural = 'Voters'


class PoliticalParty(models.Model):
    party_number = models.PositiveIntegerField(unique=True, verbose_name='Numero de lista')
    party_name = models.CharField(max_length=50, verbose_name='Nombre')
    president = models.CharField(max_length=100, verbose_name='Presidente')
    vice_president = models.CharField(max_length=100, verbose_name='Vice-presidente')
    slogan = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.party_number} - {self.party_name}'

    class Meta:
        verbose_name = 'Political Party'
        verbose_name_plural = 'Political Parties'
