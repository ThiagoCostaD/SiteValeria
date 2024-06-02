from django import forms

# sourcery skip: dont-import-test-modules
from testemunhos.models import Testemunho


class AutorTestemunhoForm(forms.ModelForm):
    class Meta:
        model = Testemunho
        fields = [
            "titulo", "autor",
            "descricao", "testemunho",
            "foto", "categoria",
            "publicado",
        ]
