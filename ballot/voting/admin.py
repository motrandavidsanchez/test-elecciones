from django.contrib import admin

from .models import Voter, PoliticalParty, Voting


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dni', 'birth_date', 'has_voted')
    search_fields = ('first_name', 'last_name', 'dni')
    list_filter = ('has_voted',)
    autocomplete_fields = ('establishment',)
    exclude = ('has_voted',)


@admin.register(PoliticalParty)
class PoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ('party_number', 'party_name', 'president', 'vice_president', 'slogan')
    search_fields = ('party_number', 'party_name')
    exclude = ('votes',)


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display = ('establishment', 'voting')
    search_fields = ('establishment',)
    list_filter = ('voting',)
    autocomplete_fields = ('establishment',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(establishment__profile__user=request.user)
