from django.urls import path

from . import views

app_name = 'testimonials'

urlpatterns = [
    path('', views.home, name='home'),

    path('testimonies/search/',
         views.search, name='search'),

    path('testimonials/category/<int:category_id>/',
         views.category, name='category'),

    path('testimonials/<int:id>/',
         views.testimony, name='testimony'),
]
