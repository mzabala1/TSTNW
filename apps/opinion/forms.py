from django import forms
from .models import Opinion

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion

        fields = [
            'escritor',
            'pregunta1',
            'pregunta2',
            'pregunta3',
        ]