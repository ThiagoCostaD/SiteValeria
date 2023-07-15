from django.test import TestCase
from django.urls import reverse


class TestemunhoURLsTest(TestCase):

    def test_testemunho_home_url_esta_correto(self):
        url = reverse('testemunhos:home')
        self.assertEqual(url, '/')

    def test_testemunho_categoria_url_esta_correto(self):
        url = reverse('testemunhos:categoria', kwargs={'categoria_id': 1})
        self.assertEqual(url, '/testemunhos/categoria/1/')

    def test_testemunho_url_esta_correto(self):
        url = reverse('testemunhos:testemunho', kwargs={'id': 1})
        self.assertEqual(url, '/testemunhos/1/')
