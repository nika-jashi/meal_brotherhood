from django import forms
from poll.models import Questionary


class BaseForm(forms.ModelForm):
    going_out = forms.BooleanField(label='out')

    class Meta:
        model = Questionary
        fields = ('going_out',)

