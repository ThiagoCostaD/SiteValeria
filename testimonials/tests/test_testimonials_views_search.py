from django.http.response import HttpResponse
from django.urls import ResolverMatch, resolve, reverse

from testimonials import views

from .test_testimonials_base import TestimonialsTestBase


class TestemunhoViewsTest(TestimonialsTestBase):

    def test_testimony_search_is_working(self) -> None:
        url: str = reverse('testimonials:search')
        resolved: ResolverMatch = resolve(url)
        self.assertIs(resolved.func, views.search)

    def test_testimony_search_load_any_template(self) -> None:
        response: HttpResponse = self.client.get(
            reverse(
                'testimonials:search'
            ) + '?search=test'
        )
        self.assertTemplateUsed(response, 'testimonies/pages/busca.html')

    def test_testemunho_busca_sem_nada_levantar_404(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('testimonials:search')
        )
        self.assertEqual(response.status_code, 404)

    def test_testimony_search_term_trim_in_title(self) -> None:
        url: str = reverse('testimonials:search') + '?search=Test'
        response: HttpResponse = self.client.get(url)
        self.assertIn(
            ' Searching for &quot;Test&quot; ',
            response.content.decode('utf-8')
        )


def test_testemunho_busca_nao_apare_o_title_buscado(self) -> None:
    title1 = "This is the one"
    title2 = 'This is two'

    testimonial1 = self.make_testimony(
        slug='one', title=title1, author_data={'username': 'one'},
    )

    testimonial2 = self.make_testimony(
        slug='two', title=title2, author_data={'username': 'two'},
    )
    search_url: str = reverse('testimonials: search')
    response1: HttpResponse = self.client.get(f'{search_url}?busca={title1}')
    response2: HttpResponse = self.client.get(f'{search_url}?busca={title2}')
    response_both: HttpResponse = self.client.get(f'{search_url}?busca=Esse')

    self.assertIn(testimonial1, response1.context['testimonials'])
    self.assertNotIn(testimonial2, response1.context['testimonials'])

    self.assertIn(testimonial2, response2.context['testimonials'])
    self.assertNotIn(testimonial1, response2.context['testimonials'])

    self.assertIn(testimonial1, response_both.context['testimonials'])
    self.assertIn(testimonial2, response_both.context['testimonials'])
