from django.shortcuts import render


def home(request):
    return render(request, 'testemunhos/pages/home.html', context={

    })
