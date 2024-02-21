from django import forms
from testemunhos.models import Testemunho


class AutorTestemunhoForm(forms.ModelForm):
    class Meta:
        model = Testemunho
        fields = ['titulo', 'autor', 'descricao', 'testemunho', 'foto', 'categoria', 'publicado']
