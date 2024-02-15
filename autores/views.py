from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import RegistroForm


def resgistro_views(request):
    register_form_data = request.session.get(
        'register_form_data', None
    )

    form = RegistroForm(register_form_data)

    return render(
        request, 'autores/pages/resgistro_views.html', {
            'form': form,
            "form_action": reverse('autores:criação'),
        }
    )


def criação_resgistro(request):

    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST

    form = RegistroForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(
            request, 'Seu usuário foi criado, por favor faça o login.')

        del (request.session['register_form_data'])

    return redirect('autores:registro')


def login_views(request):
    return render(request, 'autores/pages/login.html')


def login_create(request):
    return render(request, 'autores/pages/login_create.html')
