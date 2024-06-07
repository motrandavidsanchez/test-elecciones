from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.name


class Locality(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name='Provincia')

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return self.name


class Establishment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, verbose_name='Localidad')

    class Meta:
        verbose_name = 'Establecimiento'
        verbose_name_plural = 'Establecimientos'

    def __str__(self):
        return self.name


class Table(models.Model):
    number = models.IntegerField(verbose_name='Número de Mesa')
    establishment = models.ForeignKey(
        Establishment, on_delete=models.CASCADE, verbose_name='Establecimiento'
    )

    class Meta:
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'

    def __str__(self):
        return f'{self.number} - {self.establishment}'
