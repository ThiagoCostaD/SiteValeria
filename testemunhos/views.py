from venv import logger

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.utils.html import escape
from django.views.decorators.cache import cache_page

from .models import Testemunho


def home(request):
    testemunhos = Testemunho.objects.filter(
        publicado=True
    ).order_by('-data_criacao')
    return render(request, 'testemunhos/pages/home.html', context={
        'testemunhos': testemunhos})


def categoria(request, categoria_id):

    testemunhos = get_list_or_404(
        Testemunho.objects.filter(
            categoria__id=categoria_id,
            publicado=True
        ).order_by('-data_criacao')
    )

    return render(request, 'testemunhos/pages/categoria.html', context={
        'testemunhos': testemunhos,
        'titulo': f'{testemunhos[0].categoria.nome} - Categoria |'
    })


@cache_page(60*15)
def testemunho(request, id):

    try:
        testemunho = get_object_or_404(Testemunho, pk=id, publicado=True)
    except Http404:
        logger.error('Testemunho not found with id %s', id)
        raise

    return render(request, 'testemunhos/pages/testemunho-view.html', context={
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

    testemunho = Testemunho.objects.filter(
        Q(
            Q(titulo__icontains=termo_busca) |
            Q(descricao__icontains=termo_busca),
        ),
        publicado=True,
    ).order_by('-id')

    resultados = []  # search results
    paginator = Paginator(resultados, 10)  # 10 results per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'testemunhos/pages/busca.html', {
        'titulo_pagina': f'Pesquisando por "{termo_busca}"  ',
        'page_obj': page_obj,
        'termo_busca': termo_busca,
        'testemunhos': testemunho,
    }
    )
