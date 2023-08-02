from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegistroForm


def resgistro_views(request):
    register_form_data = request.session.get(
        'register_form_data', None
    )

    form = RegistroForm(register_form_data)

    return render(
        request, 'autores/pages/resgistro_views.html', {
            'form': form,
        }
    )


def criação_resgistro(request):

    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST

    form = RegistroForm(POST)

    return redirect('autores:registro')
