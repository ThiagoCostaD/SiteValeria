import os
from venv import logger

# from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils.html import escape
from django.views.generic import ListView

from utils.pagination import make_pagination

from .models import Testemunho

PER_PAGE = int(os.environ.get('PER_PAGE', 9))


class TestemunhoListViewBase(ListView):
    model = Testemunho
    context_object_name = 'testemunhos'
    ordering = ['-id']
    template_name = 'testemunhos/pages/home.html'
    queryset = Testemunho.objects.filter(publicado=True)

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


def testemunho(request, id):

    try:
        testemunho = get_object_or_404(Testemunho, pk=id, publicado=True)
    except Http404:
        logger.error('Testemunho not found with id %s', id)
        raise

    return render(request, 'testemunhos/pages/testemunho-view.html',
                  context={
                      'testemunho': testemunho,
                      'pagina_detalhada': True,
                  })


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
