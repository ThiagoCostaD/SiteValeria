from django.urls import path

from . import views

app_name = "testemunhos"

urlpatterns = [
    path(
        "",
        views.TestemunhoListViewHome.as_view(),
        name="home"
    ),
    path(
        "testemunhos/busca/",
        views.TestemunhoListViewBusca.as_view(),
        name="busca"
    ),
    path(
        "testemunhos/categoria/<int:categoria_id>/",
        views.TestemunhoListViewCategoria.as_view(),
        name="categoria"
    ),
    path(
        "testemunhos/<int:id>/",
        views.testemunho,
        name="testemunho"
    ),
]
