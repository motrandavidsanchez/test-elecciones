from django.contrib import admin

from .models import Province, Locality, Establishment, Table


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ['name', 'province']


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'locality']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['number', 'establishment']
