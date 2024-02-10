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
    def test_fist_name_placeholder_is_correct(self, field, placeholder):
        form = RegistroForm()
        current_placeholder = form[field].fields.widget.attrs['placeholder']
        self.assertEqual(placeholder, current_placeholder)
