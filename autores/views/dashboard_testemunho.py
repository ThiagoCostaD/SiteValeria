from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from pyexpat.errors import messages

from autores.forms.testemunho_form import AutorTestemunhoForm
# sourcery skip: dont-import-test-modules
from testemunhos.models import Testemunho


class DashboardTestemunho(View):
    def get_testemunho(self, id):
        testemunho = None

        if id:
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

    def get(self, *args, **kwargs):

        testemunho = self.get_testemunho(kwargs.get("id"))

        form = AutorTestemunhoForm(isinstance=testemunho)

        return self.render_testemunho(form)

    def post(self, request, id):  # sourcery skip: extract-method
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
                    args=(id,)
                )
            )

        return self.render_testemunho(form)
