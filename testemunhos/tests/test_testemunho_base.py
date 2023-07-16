from django.contrib.auth.models import User
from django.test import TestCase
from testemunhos.models import Categoria, Testemunho


class TestemunhoTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_categoria(self, nome='Catergoria'):
        return Categoria.objects.create(nome=nome)

    def make_autor(self, first_name='user',
                   last_name='name', username='username',
                   password='123456', email='user@email.com'
                   ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )

    def make_testemunho(self,
                        categoria_data=None,
                        autor_data=None,
                        titulo='Testemunho titulo',
                        descricao='Descrição Testemunho',
                        slug='Testemunho-slug',
                        testemunho='Testemunho',
                        publicado=True,
                        ):
        if categoria_data is None:
            categoria_data = {}

        if autor_data is None:
            autor_data = {}

        return Testemunho.objects.create(
            categoria=self.make_categoria(**categoria_data),
            autor=self.make_autor(**autor_data),
            titulo=titulo,
            descricao=descricao,
            slug=slug,
            testemunho=testemunho,
            publicado=publicado,
        )
