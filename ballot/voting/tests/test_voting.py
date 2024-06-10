import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client

from geodirectory.tests.factories import EstablishmentFactory
from voting.models import Voting
from voting.tests.factories import VoterFactory


@pytest.mark.django_db
class TestCheckDNIView:
    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        self.client = Client()
        self.establishment = EstablishmentFactory(name='Test Establishment')
        self.voter = VoterFactory(dni='12345678', establishment=self.establishment)
        self.voting = Voting.objects.create(establishment=self.establishment, voting=True)
        self.mocker = mocker

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_dni_exists_and_user_not_voted(self):
        self.mocker.patch('voting.views.has_voted', return_value=True)

        response = self.client.post(reverse('check-dni'), {'dni': '12345678'})
        assert response.status_code == 302
        assert response.url == reverse('political-party', kwargs={'dni': '12345678'})

    def test_dni_exists_and_user_already_voted(self, mocker):
        mocker.patch('voting.views.has_voted', return_value=False)

        response = self.client.post(reverse('check-dni'), {'dni': '12345678'})
        assert response.status_code == 200
        assert 'Usted ya emitio el voto.' in response.content.decode()

    def test_dni_does_not_exist(self):
        response = self.client.post(reverse('check-dni'), {'dni': '87654321'})
        assert response.status_code == 200
        assert 'DNI no encontrado en el padrón.' in response.content.decode()

    def test_voting_closed(self, mocker):
        self.voting.voting = False
        self.voting.save()

        mocker.patch('voting.views.has_voted', return_value=True)

        response = self.client.post(reverse('check-dni'), {'dni': '12345678'})
        assert response.status_code == 200
        assert 'Ya cerraron las votaciones del establecimiento.' in response.content.decode()
