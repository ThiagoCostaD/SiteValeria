from cgi import test
from unittest.mock import patch

from django.urls import resolve, reverse

from testimonials import views

from .test_testimonials_base import TestimonialsTestBase


class TestemunhoViewsHomeTest(TestimonialsTestBase):

    def test_testemunho_home_view_esta_operando(self):
         view = resolve(reverse('testimonials:home'))
         self.assertIs(view.func, views.home)

    def test_test_home_view_retorna_status_200_ok(self):
        response = self.client.get(reverse('testimonials:home'))
        self.assertEqual(response.status_code, 200)

    def test_test_home_view_loads_correct_template(self):
        response = self.client.get(reverse('testimonials:home'))
        self.assertTemplateUsed(response, 'testimonials/pages/home.html')

    def test_test_test_home_sem_testimony(self):
        response = self.client.get(reverse('testimonials:home'))
        self.assertIn(
            'We don't have any testimony for now, come back soon'\
            response.content.decode('utf-8')
            )

    def test_testimonies_home_templates_load_testimony(self):
        self.make_testimony()
        response = self.client.get(reverse('testimonials:home'))
        response_testimonials = response.context['testimonials']
        content = response.content.decode('utf-8')

        self.assertEqual(
            len(response.context
                ['testimonies']), 1
        ),
        self.assertEqual(
            response_Testimony.first().title,
            'Title testimony'
        ),
        self.assertIn('Testimony title', content)
        self.assertIn('Testimony', content)

    def test_test_test_home_not_published(self):
        """testing whether testimonials that are marked as unpublished pass the test""" # noqa: E501
        self.make_testimony(published=False)
        response = self.client.get(reverse('testimonials:home'))

        self.assertIn(
            'We don't have any testimony for now, come back soon',
            response.content.decode('utf-8')
        )

    def test_testemunho_home_esta_paginando(self):
        for i in range(9):
            kwargs = {'slug': f'r{i}', 'author': {'username': f'u{i}'}}
            self.make_testimony(**kwargs)

        with patch('testimonies.views.PER_PAGE', new=3):
            response = self.client.get(reverse('testimonials:home'))
            testimonials = response.context['testimonials']
            paginator = testimonials.paginator

            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)
