from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_testemunho_base import Testemunho, TestemunhoTestBase


class TestemunhoModelTest(TestemunhoTestBase):
    def setUp(self) -> None:
        self.testemunho = self.make_testemunho()
        return super().setUp()

    def make_testemunho_no_defaults(self):
        testemunho = Testemunho(
            categoria=self.make_categoria(nome='Testar o padrão categoria'),
            autor=self.make_autor(username='newuser'),
            titulo='Testemunho titulo',
            descricao='Descrição Testemunho',
            slug='Testemunho-slug',
            testemunho='Testemunho',
            publicado=True,
            foto=None
        )
        testemunho.full_clean()
        testemunho.save()
        return testemunho

    @parameterized.expand([
        ('titulo', 77),
        ('descricao', 165)
    ])
    def test_testemunho_todos_campos_max_length(self, campo, max_length):
        setattr(self.testemunho, campo, 'A' * (max_length + 10))
        with self.assertRaises(ValidationError):
            self.testemunho.full_clean()

    def test_testemunho_representação_string(self):
        frase = 'Teste representação'
        self.testemunho.titulo = 'Teste representação'
        # self.testemunho.full_clean()
        self.testemunho.save()
        self.assertEqual(
            str(self.testemunho), frase,
            msg=f'a representação da string da receita deve ser '
                f'"{frase}" mas chegou isso "{str(self.testemunho)}" '
        )
