from django.shortcuts import render
# from utils.testemunhos.fabrica import make_testemunho
from .models import Testemunho


def home(request):
    testemunhos = Testemunho.objects.filter(
        publicado=True
    ).order_by('id')
    return render(request, 'testemunhos/pages/home.html', context={
        'testemunhos': testemunhos})


def categoria(request, categoria_id):
    testemunhos = Testemunho.objects.filter(
        categoria__id=categoria_id,
        publicado=True
    ).order_by('-id')
    return render(request, 'testemunhos/pages/home.html', context={
        'testemunhos': testemunhos})


def testemunho(request, id):
    testemunhos = Testemunho.objects.filter(
        publicado=True
    )
    return render(request, 'testemunhos/pages/testemunho-view.html', context={
        'testemunho': testemunhos(),
        'pagina_detalhada': True,
    })
