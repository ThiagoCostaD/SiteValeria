from django.core.exceptions import ValidationError

from .test_testemunho_base import TestemunhoTestBase


class TestemunhoModelCatergoriaTest(TestemunhoTestBase):
    def setUp(self) -> None:
        self.categoria = self.make_categoria(
            nome='Testando Categoria'
        )
        return super().setUp()

    def test_testemunho_categoria_representação_string(self):
        self.assertEqual(
            str(self.categoria),
            self.categoria.nome
        )

    def test_testemunho_categoria_model_max_length(self):
        self.categoria.nome = 'A' * 51
        with self.assertRaises(ValidationError):
            self.categoria.full_clean()
