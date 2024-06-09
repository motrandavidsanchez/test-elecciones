from django.views.generic import TemplateView


class PoliticalPartyView(TemplateView):
    template_name = 'voting/political-party.html'
