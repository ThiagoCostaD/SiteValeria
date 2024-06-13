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
        "testemunhos/<int:pk>/",
        views.TestemunhoDetail.as_view(),
        name="testemunho"
    ),
    path(
        "testemunhos/api/v1/",
        views.TestemunhoListViewHomeApi.as_view(),
        name="testemunho_api_v1"
    ),
    path(
        "testemunhos/api/v1/<int:pk>/",
        views.TestemunhoDetailApi.as_view(),
        name="testemunho_api_v1_detail"
    ),
]
