from venv import logger
from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404

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
