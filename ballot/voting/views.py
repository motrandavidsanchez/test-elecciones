from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, FormView

from voting.forms import DNICheckForm
from voting.models import PoliticalParty, Voter, Voting
from voting.utils import (
    has_voted_percentage,
    has_voted,
    all_voting_false,
    all_voting_false_percentage,
)


class IndexView(TemplateView):
    template_name = 'voting/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_voters = Voter.objects.count()

        context['political_parties'] = PoliticalParty.objects.all()
        context['total_voters'] = total_voters
        context['stake'] = has_voted_percentage()
        context['voting'] = all_voting_false()
        context['total_voting'] = all_voting_false_percentage()
        return context


class CheckDNIView(LoginRequiredMixin, FormView):
    template_name = 'voting/check_dni.html'
    form_class = DNICheckForm

    def form_valid(self, form):
        try:
            dni = form.cleaned_data['dni']
            voter = Voter.objects.get(dni=dni)
            establishment = voter.establishment
            voting = Voting.objects.get(establishment=establishment)

            if has_voted(dni):
                form.add_error('dni', 'Usted ya emitio el voto.')
                return self.form_invalid(form)

            if not voting.voting:
                form.add_error('dni', 'Ya cerraron las votaciones del establecimiento.')
                return self.form_invalid(form)

            return redirect('political-party', dni=dni)
        except Voter.DoesNotExist:
            form.add_error('dni', 'DNI no encontrado en el padrón.')
            return self.form_invalid(form)


class PoliticalPartyView(LoginRequiredMixin, TemplateView):
    template_name = 'voting/political-party.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['political_parties'] = PoliticalParty.objects.all()
        context['dni'] = self.kwargs['dni']
        return context


class VoteView(View):
    def post(self, request, *args, **kwargs):
        dni = request.POST.get('dni')
        party_id = request.POST.get('party')
        Voter.objects.filter(dni=dni).update(has_voted=True)
        political_party = PoliticalParty.objects.get(id=int(party_id))
        political_party.sum_votes()
        return redirect('check-dni')
