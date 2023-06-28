from django.shortcuts import render


def home(request):
    return render(request, 'testemunhos/home.html', context={

    })
