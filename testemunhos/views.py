import os
from venv import logger

# from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
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


def home(request):
    testemunhos = Testemunho.objects.filter(
        publicado=True
    ).order_by('-data_criacao')

    page_obj, pagination_range = make_pagination(
        request, testemunhos, PER_PAGE)

    return render(request, 'testemunhos/pages/home.html', context={
        'testemunhos': page_obj,
        'pagination_range': pagination_range,
    })


def categoria(request, categoria_id):

    testemunhos = get_list_or_404(
        Testemunho.objects.filter(
            categoria__id=categoria_id,
            publicado=True
        ).order_by('-data_criacao')
    )

    page_obj, pagination_range = make_pagination(
        request, testemunhos, PER_PAGE)

    return render(request, 'testemunhos/pages/categoria.html',
                  context={
                      'testemunhos': page_obj,
                      'pagination_range': pagination_range,
                      'titulo': f'{testemunhos[0].categoria.nome} - Categoria |'  # noqa: E501
                  })


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


def busca(request):
    termo_busca = escape(
        request.GET.get(
            'busca', ''
        ).strip()
    )

    if not termo_busca:
        raise Http404()

    testemunhos = Testemunho.objects.filter(
        Q(
            Q(titulo__icontains=termo_busca) |
            Q(descricao__icontains=termo_busca),
        ),
        publicado=True,
    ).order_by('-data_criacao')

    page_obj, pagination_range = make_pagination(
        request, testemunhos, PER_PAGE)

    return render(request, 'testemunhos/pages/busca.html',
                  {
                      'titulo_pagina': f'Pesquisando por "{termo_busca}"  ',
                      'termo_busca': termo_busca,
                      'testemunhos': page_obj,
                      'pagination_range': pagination_range,
                      'additional_url_query': f'&busca={termo_busca}',
                  }
                  )
