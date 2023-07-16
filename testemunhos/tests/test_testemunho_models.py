from .test_testemunho_base import TestemunhoTestBase


class TestemunhoModelTest(TestemunhoTestBase):
    def setUp(self) -> None:
        self.testemunho = self.make_testemunho()
        return super().setUp()
