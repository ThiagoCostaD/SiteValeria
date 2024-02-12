from multiprocessing import current_process

from django.test import TestCase
from parameterized import parameterized

from autores.forms import RegistroForm


class AutorRegistroFormUnitTest(TestCase):

    @parameterized.expand([
        ('username', 'Seu nome de usuário'),
        ('email', 'Seu e-mail'),
        ('first_name', 'Ex.: John'),
        ('last_name', 'Ex.: Doe'),
        ('password', 'Sua senha'),
        ('password2', 'Repita a sua senha'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = RegistroForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand([
        ('username', (
            'Obrigatório. 150 caracteres ou menos. '
            'Letras, números e @/./+/-/_ apenas.')),
        ('password', (
            'A senha deve ter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. O comprimento deve ser '
            'pelo menos 8 caracteres.'
        )),
        ('email', 'O e-mail deve ser válido.'),

    ])
    def test_fields_help_text(self, field, needed):
        form = RegistroForm()
        current = form[field].fields.fields_help
        self.assertEqual(current, needed)

    @parameterized.expand([
        ('username', 'Nome de usuário'),
        ('first_name', 'Nome'),
        ('last_name', 'Sobrenome'),
        ('email', 'E-mail'),
        ('password', 'Senha'),
    ])
    def test_fields_label(self, field, needed):
        form = RegistroForm()
        current = form[field].fields.label
        self.assertEqual(current, needed)
