from django.contrib import admin

from .models import Voter, PoliticalParty


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dni', 'birth_date', 'has_voted')
    search_fields = ('first_name', 'last_name', 'dni')
    list_filter = ('has_voted',)


@admin.register(PoliticalParty)
class PoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ('party_number', 'party_name', 'president', 'vice_president', 'slogan')
    search_fields = ('party_number', 'party_name')
    exclude = ('votes',)
