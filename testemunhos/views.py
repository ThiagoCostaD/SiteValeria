from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Testemunho


def home(request):
    testemunhos = Testemunho.objects.filter(
        publicado=True
    ).order_by('id')
    return render(request, 'testemunhos/pages/home.html', context={
        'testemunhos': testemunhos})


def categoria(request, categoria_id):

    testemunhos = get_list_or_404(
        Testemunho.objects.filter(
            categoria__id=categoria_id,
            publicado=True
        ).order_by('-id')
    )

    return render(request, 'testemunhos/pages/categoria.html', context={
        'testemunhos': testemunhos,
        'titulo': f'{testemunhos[0].categoria.nome} - Categoria |'
    })


def testemunho(request, id):

    testemunho = get_object_or_404(Testemunho, pk=id, publicado=True)

    return render(request, 'testemunhos/pages/testemunho-view.html', context={
        'testemunho': testemunho,
        'pagina_detalhada': True,
    })
