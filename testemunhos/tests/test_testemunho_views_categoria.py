from django.urls import resolve, reverse

from testemunhos import views

from .test_testemunho_base import TestemunhoTestBase


class TestemunhoViewsCategoriaTest(TestemunhoTestBase):
    def test_testemunho_categoria_view_esta_funcionando(self):
        view = resolve(
            reverse(
                'testemunhos:categoria',
                kwargs={
                    'categoria_id': 1000
                }
            )
        )
        self.assertIs(view.func, views.categoria)

    def test_testemunho_categoria_view_retorna_404_se_não_tiver_testemunhos(self):  # noqa: E501
        response = self.client.get(
            reverse(
                'testemunhos:categoria',
                kwargs={
                    'categoria_id': 10000
                }
            )
        )
        self.assertEqual(response.status_code, 404)

    def test_testemunhos_categoria_templates_carrega_testemunho(self):
        o_titulo = 'Esse é o teste da categoria'

        self.make_testemunho(titulo=o_titulo)
        response = self.client.get(
            reverse(
                'testemunhos:categoria',
                args=(1, )
            )
        )
        content = response.content.decode('utf-8')

        self.assertIn(o_titulo, content)

    def test_testemunhos_categoria_não_publicada(self):
        """testando se os testemunhos que estão marcados como não publicdos passam no teste"""  # noqa: E501
        testemunho = self.make_testemunho(publicado=False)

        response = self.client.get(
            reverse(
                'testemunhos:testemunho',
                kwargs={
                    'id': testemunho.categoria.id
                }
            )
        )
        self.assertEqual(response.status_code, 404)
