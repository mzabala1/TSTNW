from django import forms
from .models import Opinion


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion

        fields = [
            'pre1',
            'pre2',
            'pre3',
        ]
