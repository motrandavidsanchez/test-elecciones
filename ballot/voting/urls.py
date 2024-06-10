from django.urls import path

from voting.views import PoliticalPartyView, CheckDNIView, VoteView

urlpatterns = [
    path('check-dni', CheckDNIView.as_view(), name='check-dni'),
    path('political-party/<int:dni>/', PoliticalPartyView.as_view(), name='political-party'),
    path('vote/', VoteView.as_view(), name='vote'),
]
