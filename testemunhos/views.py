# flake8: noqa
import os

from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import Http404, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.utils.html import escape
from django.views.generic import DetailView, ListView

from utils.pagination import make_pagination

from .models import Testemunho

PER_PAGE = int(os.environ.get('PER_PAGE', 9))


class TestemunhoListViewBase(ListView):
    model = Testemunho
    context_object_name = 'testemunhos'
    ordering = ['-id']
    template_name = 'testemunhos/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(publicado=True)
        qs = qs.prefetch_related('categoria', 'autor')

        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(
            self.request,
            ctx.get('testemunhos'),
            PER_PAGE
        )

        ctx.update({
            'testemunhos': page_obj,
            'pagination_range': pagination_range,
        })
        return ctx


class TestemunhoListViewHome(TestemunhoListViewBase):
    template_name = 'testemunhos/pages/home.html'


class TestemunhoListViewHomeApi(TestemunhoListViewBase):
    template_name = 'testemunhos/pages/home.html'

    def render_to_response(self, context, **response_kwargs):
        testemunhos = self.get_context_data()['testemunhos']
        testemunhos_dict = testemunhos.object_list.values()

        return JsonResponse(
            list(testemunhos_dict),
            safe=False
        )


class TestemunhoListViewCategoria(TestemunhoListViewBase):
    template_name = 'testemunhos/pages/categoria.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            categoria__id=self.kwargs.get('categoria_id')
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update({
            'titulo': f'{self.get_queryset().first().categoria.nome} - Categoria |'  # noqa: E501
        })
        return ctx


class TestemunhoListViewBusca(TestemunhoListViewBase):
    template_name = 'testemunhos/pages/busca.html'

    def get_queryset(self):

        if termo_busca := escape(self.request.GET.get('busca', '').strip()):
            return super().get_queryset().filter(
                Q(
                    Q(titulo__icontains=termo_busca) |
                    Q(descricao__icontains=termo_busca),
                ),
            )
        else:
            raise Http404()


class TestemunhoDetail(DetailView):
    model = Testemunho
    context_object_name = 'testemunho'
    template_name = 'testemunhos/pages/testemunho-view.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update({
            'pagina_detalhada': True,
        })
        return ctx


class TestemunhoDetailApi(TestemunhoDetail):
    def render_to_response(self, context, **response_kwargs):
        testemunho = self.get_context_data()['testemunho']
        testemunho_dict = model_to_dict(testemunho)

        if testemunho_dict.get('foto'):
            testemunho_dict['foto'] = self.request.build_absolute_uri(
            ) + testemunho_dict['foto'].url[1:]
        else:
            testemunho_dict['foto'] = ''

        del testemunho_dict['publicado']

        return JsonResponse(
            testemunho_dict,
            safe=False
        )
