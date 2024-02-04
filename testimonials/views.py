import os
from venv import logger

# from django.contrib import messages
from django.db.models import Q
from django.db.models.manager import BaseManager
from django.db.utils import OperationalError
from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.utils.html import escape
from django.utils.safestring import SafeText

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


def category(request, category_id) -> HttpResponse:

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


def search(request) -> HttpResponse:
    term_search: SafeText = escape(
        request.GET.get(
            'search', ''
        ).strip()
    )

    if not term_search:
        raise Http404()

    testimonials = testimony.objects.filter(
        Q(
            Q(titulo__icontains=term_search)
            | Q(descricao__icontains=term_search),
        ),
        publicado=True,
    ).order_by('-date_creation')

    page_obj, pagination_range = make_pagination(
        request, testimonials, PER_PAGE)

    return render(request, 'testimonials/pages/search.html',
                  {
                      'titulo_pagina': f'Searching for "{term_search}"  ',
                      'term_search': term_search,
                      'testimonials': page_obj,
                      'pagination_range': pagination_range,
                      'additional_url_query': f'&search={term_search}',
                  }
                  )
