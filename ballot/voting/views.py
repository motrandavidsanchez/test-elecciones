from django.views.generic import TemplateView

from voting.models import PoliticalParty


class IndexView(TemplateView):
    template_name = 'voting/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['political_parties'] = PoliticalParty.objects.all()
        return context


class PoliticalPartyView(TemplateView):
    template_name = 'voting/political-party.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['political_parties'] = PoliticalParty.objects.all()
        return context
