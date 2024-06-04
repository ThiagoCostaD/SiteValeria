from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from autores.forms import AutorTestemunhoForm, LoginForm, RegistroForm
# sourcery skip: dont-import-test-modules
from testemunhos.models import Testemunho


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
        return _extracted_from_criação_resgistro_12(form, request)
    return redirect('autores:registro')


def _extracted_from_criação_resgistro_12(form, request):
    user = form.save(commit=False)
    user.set_password(user.password)
    user.save()
    messages.success(
        request, 'Seu usuário foi criado, por favor faça o login.')

    del (request.session['register_form_data'])
    return redirect(reverse('autores:login'))


def login_views(request):
    form = LoginForm()
    return render(
        request,
        'autores/pages/login.html',
        {'form': form,
         'form_action': reverse('autores:login_create'),
         }
    )


def login_create(request):

    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )
        if authenticated_user is not None:
            messages.success(request, 'Your are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid username or password')

    return redirect(reverse('autores:dashboard'))


@login_required(login_url='autores:login', redirect_field_name='next')
def logout_view(request):

    if not request.POST:
        return redirect(reverse('autores:login'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('autores:login'))
    logout(request)
    return redirect(reverse('autores:login'))


@login_required(login_url='autores:login', redirect_field_name='next')
def dashboard(request):
    testemunhos = Testemunho.objects.filter(

        autor=request.user
    )
    return render(
        request,
        'autores/pages/dashboard.html',
        context={
            'testemunhos': testemunhos,
        }
    )


@login_required(login_url='autores:login', redirect_field_name='next')
def dashboard_testemunho_create(request) -> HttpResponse:

    form = AutorTestemunhoForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if form.is_valid():
        testemunho = form.save(commit=False)

        testemunho.autor = request.user
        testemunho.preparation_step_is_html = False
        testemunho.is_published = False

        testemunho.save()

        messages.success(request, 'Testemunho criado com sucesso.')
        return redirect(
            reverse(
                'autores:dashboard_testemunho_edit',
                args=(
                    testemunho.pk,
                )
            )
        )

    return render(
        request,
        'autores/pages/dashboard_testemunho.html',
        context={
            'form': form,
        }
    )
