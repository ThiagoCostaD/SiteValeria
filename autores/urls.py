from django.urls import path

from . import views

urlpatterns = [
    path('registro/', views.resgistro_views, name='resgistro'),
]
