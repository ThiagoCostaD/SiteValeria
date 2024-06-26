from django.urls import path

from . import views

app_name = 'autores'

urlpatterns = [
    path('registro/', views.resgistro_views, name='registro'),
    path('registro/criação/', views.criação_resgistro, name='criação'),
    path('login/', views.login_views, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path(
        'dashboard/testemunho/new/',
        views.DashboardTestemunho.as_view(),
        name='dashboard_testemunho_new'
    ),
    path(
        'dashboard/testemunho/delete/',
        views.DashboardTestemunhoDelete.as_view(),
        name='dashboard_testemunho_delete'
    ),
    path(
        'dashboard/testemunho/<int:id>/edit/',
        views.DashboardTestemunho.as_view(),
        name='dashboard_testemunho_edit'
    ),

]
