from django.http.response import HttpResponse
from django.urls import ResolverMatch, resolve, reverse

from testimonials import views

from .test_testimonials_base import TestimonialsTestBase


class TestimonyViewsDetailedTest(TestimonialsTestBase):

    def test_test_view_detailed_is_working(self) -> None:
        view: ResolverMatch = resolve(
            reverse(
                'testimonies:testimony',
                kwargs={
                    'id': 1
                }
            )
        )
        self.assertIs(view.func, views.testimony)

    def test_test_test_view_detailed_retorna_404_se_não_tiver_testimonhos(self) -> None:  # noqa: E501
        response: HttpResponse = self.client.get(
            reverse(
                'testimonies:testimony',
                kwargs={
                    'id': 10000
                }
            )
        )
        self.assertEqual(response.status_code, 404)

    def test_test_test_detailed_load_testimony(self) -> None:
        the_title = 'This is the detailed page test'

        self.make_testimony(title=the_title)
        response: HttpResponse = self.client.get(
            reverse(
                'testimonies:testimony',
                kwargs={
                    'id': 1
                }
            )
        )
        content: str = response.content.decode('utf-8')

        self.assertIn(the_title, content)

    def test_detailed_testimonies_unpublished(self):
        """testing whether testimonials that are marked as unpublished pass the test"""  # noqa: E501
        testimony = self.make_testimony(published=False)

        response: HttpResponse = self.client.get(
            reverse(
                'testimonies:testimony',
                kwargs={
                    'id': testimony.id
                }
            )
        )
        self.assertEqual(response.status_code, 404)
