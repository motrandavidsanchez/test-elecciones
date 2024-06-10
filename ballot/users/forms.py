from typing import Any

from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.db import transaction

from geodirectory.models import Establishment
from .models import Profile


class CustomUserChangeForm(UserChangeForm):
    dni = forms.CharField(required=True, label='DNI')
    establishment = forms.ModelChoiceField(
        Establishment.objects.all(),
        required=False,
        label='Establecimiento',
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'profile'):
            self.fields['dni'].initial = self.instance.profile.dni
            self.fields['establishment'].initial = self.instance.profile.establishment

    @transaction.atomic()
    def save(self, commit=True) -> Any:
        user: User = super().save(commit)
        dni = self.cleaned_data.get('dni')
        establishment = self.cleaned_data.get('establishment', None)
        profile, *_ = Profile.objects.update_or_create(
            user_id=user.pk,
            defaults=dict(
                dni=dni,
                establishment=establishment,
            ),
        )
        return user
