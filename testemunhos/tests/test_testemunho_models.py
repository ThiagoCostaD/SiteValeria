from django.core.exceptions import ValidationError

from .test_testemunho_base import TestemunhoTestBase


class TestemunhoModelTest(TestemunhoTestBase):
    def setUp(self) -> None:
        self.testemunho = self.make_testemunho()
        return super().setUp()

    def test_titulo_testemunho_erro_acima_de_77_caracteres(self):
        self.testemunho.titulo = 'A' * 78

        with self.assertRaises(ValidationError):
            self.testemunho.full_clean()
