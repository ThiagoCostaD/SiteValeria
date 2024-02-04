from django.test import TestCase
from django.urls import reverse


class TestimonyURLsTest(TestCase):

    def test_testemunho_home_url_esta_correto(self):
        url = reverse('testimonials:home')
        self.assertEqual(url, '/')

    def test_testemunho_categoria_url_esta_correto(self):
        url = reverse('testimonials:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/testimonials/category/1/')

    def test_testemunho_url_esta_correto(self):
        url = reverse('testimonials:testimony', kwargs={'id': 1})
        self.assertEqual(url, '/testimonies/1/')

    def test_url_de_busca_esta_ok(self):
        url = reverse('testimonials:search')
        self.assertEqual(url, '/testimonies/search/')
