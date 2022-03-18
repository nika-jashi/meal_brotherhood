from django import forms
from poll.models import Menu


class BaseForm(forms.ModelForm):
    going_out = forms.BooleanField(label='out')

    class Meta:
        model = Menu
        fields = ('going_out',)

