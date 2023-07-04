from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('testemunhos/<slug:id>/', views.testemunho),
]
