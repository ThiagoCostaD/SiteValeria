import re
from typing import Any

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from genericpath import exists


def add_attr(field, attr_name, attr_new_val) -> None:
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val) -> None:
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password) -> None:
    regex: re.Pattern[str] = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter, one lowercase letter and one number. The length should be at least 8 characters.'
        ),
            code='Invalid'
        )


class RegistroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu nome de usuário')
        add_placeholder(self.fields['email'], 'Seu e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_placeholder(self.fields['password'], 'Sua senha')
        add_placeholder(self.fields['password2'], 'Repita a sua senha')

    username = forms.CharField(
        label='Nome de usuário',
        help_text=(
            'Obrigatório. 150 caracteres ou menos.'
            'Letras, números e @ . + -_.'),
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 150 characters',
        },
        min_length=4, max_length=150,
    )

    first_name = forms.CharField(
        error_messages={'required': 'Escreva seu primeiro nome'},
        label='Nome',
    )

    last_name = forms.CharField(
        error_messages={'required': 'Escreva seu sobrenome'},
        label='Sobrenome',
    )

    email = forms.EmailField(
        error_messages={'required': 'O e-mail não deve estar vazio'},
        help_text='O e-mail deve ser válido.',
        label='E-mail',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        },
        help_text=(
            'A senha deve ter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. O comprimento deve ser '
            'pelo menos 8 caracteres.'
        ),
        validators=[strong_password],
        label='Senha',
    )
    password2 = forms.CharField(
        error_messages={
            'required': 'Repita a sua senha'
        },
        label='Repita a sua senha',
    )

    class Meta:
        model = User
        fields: list[str] = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels: dict[str, str] = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )

        return email

    def clean(self) -> None:
        cleaned_data: dict[str, Any] = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and Password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
