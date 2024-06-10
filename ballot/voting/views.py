from django.views.generic import TemplateView

from voting.models import PoliticalParty, Voter
from voting.utils import has_voted_percentage


class IndexView(TemplateView):
    template_name = 'voting/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_voters = Voter.objects.count()

        context['political_parties'] = PoliticalParty.objects.all()
        context['total_voters'] = total_voters
        context['stake'] = has_voted_percentage()
        return context


class PoliticalPartyView(TemplateView):
    template_name = 'voting/political-party.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['political_parties'] = PoliticalParty.objects.all()
        return context
