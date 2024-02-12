from unittest import TestCase

from django.test import TestCase as DjangoTestCase
from django.urls import reverse
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
        ('email', 'O e-mail deve ser válido.'),
        ('password', (
            'A senha deve ter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. O comprimento deve ser '
            'pelo menos 8 caracteres.'
        )),
    ])
    def test_fields_help_text(self, field, needed):
        form = RegistroForm()
        current = form[field].field.help_text
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
        current = form[field].field.label
        self.assertEqual(current, needed)


class AutorRegistroFormIntegrationTest(DjangoTestCase):

    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@email.com',
            'password': 'F4k3P@ssw0rd',
            'password2': 'F4k3P@ssw0rd',
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand([
        ('username', 'Este campo não deve estar vazio'),
        ('first_name', 'Escreva seu primeiro nome'),
        ('last_name', 'Escreva seu sobrenome'),
        ('password', 'A senha não deve estar vazia'),
        ('password2', 'Repita a sua senha'),
        ('email', 'O e-mail não deve estar vazio'),


    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('autores:criação')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(field))
