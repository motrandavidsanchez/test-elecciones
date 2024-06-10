import factory
from factory import django, Faker

from geodirectory.models import Locality, Province, Establishment


class ProvinceFactory(django.DjangoModelFactory):
    class Meta:
        model = Province

    name = Faker('name')


class LocalityFactory(django.DjangoModelFactory):
    class Meta:
        model = Locality

    name = Faker('name')
    province = factory.SubFactory(ProvinceFactory)


class EstablishmentFactory(django.DjangoModelFactory):
    class Meta:
        model = Establishment

    name = Faker('name')
    locality = factory.SubFactory(LocalityFactory)
