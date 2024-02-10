import re
from typing import Any

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val) -> None:
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val) -> None:
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password) -> None:
    regex: re.Pattern[str] = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'A senha deve ter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. O comprimento deve ser '
            'pelo menos 8 caracteres.'
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

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'A senha não deve estar vazia'
        },
        help_text=(
            'A senha deve ter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. O comprimento deve ser '
            'pelo menos 8 caracteres.'
        ),
        validators=[strong_password]
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repita a sua senha'
        })
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
        # exclude = ['first_name']
        labels: dict[str, str] = {
            'username': 'Nome de usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'password': 'Senha',
        }
        help_texts: dict[str, str] = {
            'email': 'O e-mail deve ser válido.',
        }
        error_messages: dict[str, dict[str, str]] = {
            'username': {
                'required': 'Este campo não deve estar vazio',
            }
        }

    def clean_password(self) -> Any | None:
        data: Any | None = self.cleaned_data.get('password')
        if 'atenção' in data:
            raise ValidationError(
                'Não digite %(pipoca)s no campo password',
                code='invalid',
                params={'pipoca': '"atenção"'}
            )
        return data

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        if 'John Doe' in data:
            raise ValidationError(
                'Não digite %(value)s no campo nome',
                code='invalid',
                params={'value': '"John Doe"'}
            )

        return data

    def clean(self) -> None:
        cleaned_data: dict[str, Any] = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Senha e senha2 devem ser iguais',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
