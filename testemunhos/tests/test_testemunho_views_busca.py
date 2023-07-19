from django.urls import resolve, reverse

from testemunhos import views

from .test_testemunho_base import TestemunhoTestBase


class TestemunhoViewsTest(TestemunhoTestBase):

    def test_testemunho_busca_esta_funcionando(self):
        url = reverse('testemunhos:busca')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.busca)

    def teste_testemunho_busca_carreg_o_template(self):
        response = self.client.get(reverse('testemunhos:busca'))
        self.assertTemplateUsed(response, 'testemunhos/pages/busca.html')
