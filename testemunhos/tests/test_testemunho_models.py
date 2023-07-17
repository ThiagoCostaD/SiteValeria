from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_testemunho_base import TestemunhoTestBase


class TestemunhoModelTest(TestemunhoTestBase):
    def setUp(self) -> None:
        self.testemunho = self.make_testemunho()
        return super().setUp()

    @parameterized.expand([
        ('titulo', 77),
        ('descricao', 165)
    ])
    def test_testemunho_todos_campos_max_length(self, campo, max_length):

        setattr(self.testemunho, campo, 'A' * (max_length + 10))
        with self.assertRaises(ValidationError):
            self.testemunho.full_clean()
