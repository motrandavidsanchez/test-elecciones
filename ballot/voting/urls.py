from django.urls import path

from voting.views import PoliticalPartyView, CheckDNIView

urlpatterns = [
    path('check-dni', CheckDNIView.as_view(), name='check-dni'),
    path('political-party', PoliticalPartyView.as_view(), name='political-party'),
]
