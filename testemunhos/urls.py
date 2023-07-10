from django.urls import path
from . import views

app_name = 'testemunhos'

urlpatterns = [
    path('', views.home, name='home'),
    path('testemunhos/categoria/<int:categoria_id>/',
         views.categoria, name='categoria'),
    path('testemunhos/<int:id>/', views.testemunho, name='testemunho'),
]
