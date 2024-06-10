from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from voting.forms import DNICheckForm
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


class CheckDNIView(FormView):
    template_name = 'voting/check_dni.html'
    form_class = DNICheckForm
    success_url = reverse_lazy('political-party')

    def form_valid(self, form):
        dni = form.cleaned_data['dni']
        try:
            Voter.objects.get(dni=dni)
            return redirect(self.success_url)
        except Voter.DoesNotExist:
            form.add_error('dni', 'DNI no encontrado en el padrón.')
            return self.form_invalid(form)


class PoliticalPartyView(TemplateView):
    template_name = 'voting/political-party.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['political_parties'] = PoliticalParty.objects.all()
        return context
