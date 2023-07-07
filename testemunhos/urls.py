from django.urls import path
from . import views

app_name = 'testemunhos'

urlpatterns = [
    path('', views.home, name='home'),
    path('testemunhos/<int:id>/', views.testemunho,
         name='testemunho'),
]
