from django import forms

from .models import Resenha

class ResenhaForm(forms.ModelForm):

    class Meta:
        model = Resenha
        fields = ('titulo', 'texto',)