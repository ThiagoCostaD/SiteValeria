from django.shortcuts import render
from utils.testemunhos.fabrica import make_testemunho


def home(request):
    return render(request, 'testemunhos/pages/home.html', context={
        'testemunhos': [make_testemunho() for _ in range(7)], })


def testemunho(request, id):
    return render(request, 'testemunhos/pages/testemunho-view.html', context={
        'testemunho': make_testemunho(),
        'pagina_detalhada': True,
    })
