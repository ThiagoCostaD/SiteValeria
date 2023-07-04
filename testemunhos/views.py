from django.shortcuts import render


def home(request):
    return render(request, 'testemunhos/pages/home.html', context={

    })


def testemunho(request, id):
    return render(request, 'testemunhos/pages/testemunho-view.html', context={

    })
