from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from pyexpat.errors import messages

from autores.forms.testemunho_form import AutorTestemunhoForm
from testemunhos.models import Testemunho


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardTestemunho(View):
    def get_testemunho(self, id=None):
        testemunho = None
        if id is not None:
            testemunho = Testemunho.objects.filter(
                pk=id,
                autor=self.request.user,
            ).first()
        if not testemunho:
            raise Http404()
        return testemunho

    def render_testemunho(self, form):
        return render(
            self.request,
            "autores/pages/dashboard_testemunho.html",
            context={
                "form": form,
            },
        )

    def get(self, id=None):

        testemunho = self.get_testemunho(id)
        form = AutorTestemunhoForm(isinstance=testemunho)
        return self.render_testemunho(form)

    def post(self, request, id=None):  # sourcery skip: extract-method
        self.request = request
        testemunho = self.get_testemunho(id)
        form = AutorTestemunhoForm(
            request.POST or None,
            files=request.FILES or None,
            instance=testemunho
        )
        if form.is_valid():
            form.save(commit=False)

            testemunho.autor = request.user
            testemunho.preparation_step_is_html = False
            testemunho.is_published = False

            testemunho.save()

            messages.success(request, "Testemunho atualizado com sucesso.")
            return redirect(
                reverse(
                    "autores:dashboard_testemunho_edit",
                    args=(
                        testemunho.id,
                    )
                )
            )
        return self.render_testemunho(form)


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardTestemunhoDelete(View):
    def post(self, *args, **kwargs):
        testemunho = self.get_testemunho(self.request.POST.get("id"))
        testemunho.delete()
        messages.success(self.request, "Testemunho deletado com sucesso.")
        return redirect(reverse("autores:dashboard"))
