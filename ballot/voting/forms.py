from django import forms


class DNICheckForm(forms.Form):
    dni = forms.IntegerField(label='DNI', min_value=0)
