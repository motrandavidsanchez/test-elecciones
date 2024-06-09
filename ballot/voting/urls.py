from django.urls import path

from voting.views import PoliticalPartyView

urlpatterns = [
    path('political-party', PoliticalPartyView.as_view()),
]
