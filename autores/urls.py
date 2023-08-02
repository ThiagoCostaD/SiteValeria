from django.urls import path

from . import views

app_name = 'autores'

urlpatterns = [
    path('registro/', views.resgistro_views, name='registro'),
    path('registro/criação/', views.criação_resgistro, name='criação'),
]
