from collections import defaultdict

from django import forms

# sourcery skip: dont-import-test-modules
from testemunhos.models import Testemunho


class AutorTestemunhoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_erros = defaultdict(list)

    class Meta:
        model = Testemunho
        fields = [
            "titulo", "autor",
            "descricao", "testemunho",
            "foto", "categoria",
            "publicado",
        ]

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cd = self.cleaned_data

        title = cd.get('titulo')
        description = cd.get('descricao')

        if len(title) < 5:
            self._my_erros['titulo'].append(
                'O título deve ter no mínimo 5 caracteres')
        if len(title) > 50:
            self._my_erros['titulo'].append(
                'O título deve ter no máximo 50 caracteres')

        if len(description) < 50:
            self._my_erros['descricao'].append(
                'A descrição deve ter no mínimo 50 caracteres')
        if title == description:
            self._my_erros['descricao'].append(
                'A descrição não pode ser igual ao título')
            self._my_erros['titulo'].append(
                'O título não pode ser igual à descrição')

        if self._my_erros:
            raise forms.ValidationError(self._my_erros)
        return super_clean
