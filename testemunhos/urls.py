from django.urls import path

from . import views

app_name = "testemunhos"

urlpatterns = [
    path(
        "",
        views.TestemunhoListViewBase.as_view(),
        name="home"
    ),
    path(
        "testemunhos/busca/",
        views.busca,
        name="busca"
    ),
    path(
        "testemunhos/categoria/<int:categoria_id>/",
        views.categoria,
        name="categoria"
    ),
    path(
        "testemunhos/<int:id>/",
        views.testemunho,
        name="testemunho"
    ),
]
