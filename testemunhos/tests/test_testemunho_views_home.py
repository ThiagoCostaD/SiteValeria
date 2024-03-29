from unittest.mock import patch

from django.urls import resolve, reverse

from testemunhos import views

from .test_testemunho_base import TestemunhoTestBase


class TestemunhoViewsHomeTest(TestemunhoTestBase):

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

    def test_testemunhos_home_templates_carrega_testemunho(self):
        self.make_testemunho()
        response = self.client.get(reverse('testemunhos:home'))
        content = response.content.decode('utf-8')
        response_testemunhos = response.context['testemunhos']

        self.assertIn('Testemunho titulo', content)
        self.assertEqual(
            len(response.context
                ['testemunhos']), 1
        ),

    def test_testemunhos_home_não_publicados(self):
        """testando se os testemunhos que estão marcados como não publicdos passam no teste"""  # noqa: E501
        self.make_testemunho(publicado=False)
        response = self.client.get(reverse('testemunhos:home'))

        self.assertIn(
            'Não temos nenhum testemunho por enquanto, volte em breve',
            response.content.decode('utf-8')
        )

    def test_testemunho_home_esta_paginando(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'autor_data': {'username': f'u{i}'}}
            self.make_testemunho(**kwargs)

        with patch('testemunhos.views.PER_PAGE', new=3):
            response = self.client.get(reverse('testemunhos:home'))
            testemunhos = response.context['testemunhos']
            paginator = testemunhos.paginator

            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)

    def test_invalid_page_query_uses_current_uses_page_one(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'autor_data': {'username': f'u{i}'}}
            self.make_testemunho(**kwargs)

        with patch('testemunhos.views.PER_PAGE', new=3):

            response = self.client.get(reverse('testemunhos:home') + '?page=1A0')
            self.assertEqual(
                response.context['testemunhos'].number,
                1
            )

            response = self.client.get(reverse('testemunhos:home') + '?page=2')
            self.assertEqual(
                response.context['testemunhos'].number,
                2
            )

            response = self.client.get(reverse('testemunhos:home') + '?page=3')
            self.assertEqual(
                response.context['testemunhos'].number,
                3
            )
