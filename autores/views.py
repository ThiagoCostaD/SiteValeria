from django.shortcuts import render

from .forms import RegistroForm


def resgistro_views(request):

    if request.POST:
        form = RegistroForm(request.POST)
    else:
        form = RegistroForm()

    return render(
        request, 'autores/pages/resgistro_views.html', {
            'form': form,
        }
    )
