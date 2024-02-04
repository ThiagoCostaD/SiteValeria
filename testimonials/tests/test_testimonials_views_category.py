from django.http.response import HttpResponse
from django.urls import ResolverMatch, resolve, reverse

from testimonials import views

from .test_testimonials_base import TestimonialsTestBase


class TestimonialViewsCategoriaTest(TestimonialsTestBase):
    def test_testemunho_categoria_view_esta_operando(self) -> None:
        view: ResolverMatch = resolve(
            reverse(
                'testimonials:category',
                kwargs={
                    'category_id': 1000
                }
            )
        )
        self.assertIs(view.func, views.category)

    def test_test_testimony_category_view_retorna_404_se_não_tiver_testimonhos(self) -> None:  # noqa: E501
        response: HttpResponse = self.client.get(
            reverse(
                'testimonials:category',
                kwargs={
                    'category_id': 10000
                }
            )
        )
        self.assertEqual(response.status_code, 404)

    def test_testimonies_category_templates_load_testimony(self):
        the_title = 'This is the category test'

        self.make_testimony(title=the_title)
        response: HttpResponse = self.client.get(
            reverse(
                'testimonials:category',
                args=(1, )
            )
        )
        content = response.content.decode('utf-8')

        self.assertIn(the_title, content)

    def test_testimonies_unpublished_category(self) -> None:
        """testing whether testimonials that are marked as unpublished pass the test"""  # noqa: E501
        testimony = self.make_testimony(published=False)

        response: HttpResponse = self.client.get(
            reverse(
                'testimonies:testimony',
                kwargs={
                    'id': testimony.category.id
                }
            )
        )
        self.assertEqual(response.status_code, 404)
