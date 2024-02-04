import os
from venv import logger

# from django.contrib import messages
from django.db.models import Q
from django.db.models.manager import BaseManager
from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.utils.html import escape

from utils.pagination import make_pagination

from .models import Testimony

PER_PAGE = int(os.environ.get('PER_PAGE', 9))


def home(request) -> HttpResponse:
    testimonials: BaseManager[Testimony] = Testimony.objects.filter(
        published=True
    ).order_by('-date_creation')

    page_obj, pagination_range = make_pagination(
        request, testimonials, PER_PAGE)

    return render(request, 'testimonials/pages/home.html', context={
        'testimonials': page_obj,
        'pagination_range': pagination_range,
    })


def category(request, categoria_id) -> HttpResponse:

    testimonials: list[Testimony] = get_list_or_404(
        Testimony.objects.filter(
            category__id=category_id,
            published=True
        ).order_by('-date_creation')
    )

    page_obj, pagination_range = make_pagination(
        request, testimonials, PER_PAGE)

    return render(request, 'testimonials/pages/category.html',
                  context={
                      'testimonials': page_obj,
                      'pagination_range': pagination_range,
                      'title': f'{testimonials[0].category.name} - Category |'  # noqa: E501
                  })


def testimony(request, id) -> HttpResponse:

    try:
        testimony: Testimony = get_object_or_404(Testimony, pk=id, publicado=True)
    except Http404:
        logger.error('testimony not found with id %s', id)
        raise

    return render(request, 'testimonials/pages/testimony-view.html',
                  context={
                      'testimony': testimony,
                      'detail_page': True,
                  })


def busca(request):
    termo_busca = escape(
        request.GET.get(
            'busca', ''
        ).strip()
    )

    if not termo_busca:
        raise Http404()

    testimonials = testimony.objects.filter(
        Q(
            Q(titulo__icontains=termo_busca)
            | Q(descricao__icontains=termo_busca),
        ),
        publicado=True,
    ).order_by('-data_criacao')

    page_obj, pagination_range = make_pagination(
        request, testimonials, PER_PAGE)

    return render(request, 'testimonials/pages/busca.html',
                  {
                      'titulo_pagina': f'Pesquisando por "{termo_busca}"  ',
                      'termo_busca': termo_busca,
                      'testimonials': page_obj,
                      'pagination_range': pagination_range,
                      'additional_url_query': f'&busca={termo_busca}',
                  }
                  )
