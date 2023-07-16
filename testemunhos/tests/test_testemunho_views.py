from django.urls import reverse, resolve
from testemunhos import views
from .test_testemunho_base import TestemunhoTestBase
from unittest import skip


class TestemunhoViewsTest(TestemunhoTestBase):

    def test_testemunho_home_view_esta_funcionando(self):
        view = resolve(reverse('testemunhos:home'))
        self.assertIs(view.func, views.home)

    def test_testemunho_home_view_retorna_status_200_ok(self):
        response = self.client.get(reverse('testemunhos:home'))
        self.assertEqual(response.status_code, 200)

    def test_testemunho_home_view_loads_correct_template(self):
        response = self.client.get(reverse('testemunhos:home'))
        self.assertTemplateUsed(response, 'testemunhos/pages/home.html')

    def test_testemunho_home_sem_testemunho(self):
        response = self.client.get(reverse('testemunhos:home'))
        self.assertIn(
            'Não temos nenhum testemunho por enquanto, volte em breve',
            response.content.decode('utf-8')
        )

    @skip('Trabalhando nisso')
    def test_testemunhos_home_templates_carrega_testemunho(self):
        self.make_testemunho()
        response = self.client.get(reverse('testemunhos:home'))
        response_testemunhos = response.context['testemunhos']
        content = response.content.decode('utf-8')

        self.assertEqual(len(response.context['testemunhos']), 1),
        self.assertEqual(response_testemunhos.first().titulo,
                         'Testemunho titulo'),
        self.assertIn('Testemunho titulo', content)
        self.assertIn('Testemunho', content)

    def test_testemunho_categoria_view_esta_funcionando(self):
        view = resolve(
            reverse('testemunhos:categoria', kwargs={'categoria_id': 1000})
        )
        self.assertIs(view.func, views.categoria)

    def test_testemunho_categoria_view_retorna_404_se_não_tiver_testemunhos(self):  # noqa: E501
        response = self.client.get(reverse(
            'testemunhos:categoria', kwargs={'categoria_id': 10000})
        )
        self.assertEqual(response.status_code, 404)

    def test_testemunho_view_detalhada_esta_funcionando(self):
        view = resolve(reverse(
            'testemunhos:testemunho', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.testemunho)

    def test_testemunho_view_detalhada_retorna_404_se_não_tiver_testemunhos(self):  # noqa: E501
        response = self.client.get(reverse(
            'testemunhos:testemunho', kwargs={'id': 10000})
        )
        self.assertEqual(response.status_code, 404)
