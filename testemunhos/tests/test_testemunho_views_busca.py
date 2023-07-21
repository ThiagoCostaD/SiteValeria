from django.urls import resolve, reverse

from testemunhos import views

from .test_testemunho_base import TestemunhoTestBase


class TestemunhoViewsTest(TestemunhoTestBase):

    def test_testemunho_busca_esta_funcionando(self):
        url = reverse('testemunhos:busca')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.busca)

    def teste_testemunho_busca_carreg_o_template(self):
        response = self.client.get(
            reverse(
                'testemunhos:busca'
            ) + '?busca=teste'
        )
        self.assertTemplateUsed(response, 'testemunhos/pages/busca.html')

    def test_testemunho_busca_sem_nada_levantar_404(self):
        response = self.client.get(
            reverse('testemunhos:busca')
        )
        self.assertEqual(response.status_code, 404)

    def test_testemunnho_busca_termo_aparece_no_titulo(self):
        url = reverse('testemunhos:busca') + '?busca=Teste'
        response = self.client.get(url)
        self.assertIn(
            ' Pesquisando por &quot;Teste&quot;   ',
            response.content.decode('utf-8')
        )

    def test_testemunho_busca_nao_aparece_o_titulo_buscado(self):
        titulo1 = "Esse é o um"
        titulo2 = 'Esse é o dois'

        testemunho1 = self.make_testemunho(
            slug='um', titulo=titulo1, autor_data={'username': 'um'},
        )

        testemunho2 = self.make_testemunho(
            slug='dois', titulo=titulo2, autor_data={'username': 'dois'},
        )
        busca_url = reverse('testemunhos:busca')
        response1 = self.client.get(f'{ busca_url }?busca={titulo1}')
        response2 = self.client.get(f'{ busca_url }?busca={titulo2}')
        response_both = self.client.get(f'{ busca_url }?busca=Esse')

        self.assertIn(testemunho1, response1.context['testemunhos'])
        self.assertNotIn(testemunho2, response1.context['testemunhos'])

        self.assertIn(testemunho2, response2.context['testemunhos'])
        self.assertNotIn(testemunho1, response2.context['testemunhos'])

        self.assertIn(testemunho1, response_both.context['testemunhos'])
        self.assertIn(testemunho2, response_both.context['testemunhos'])
