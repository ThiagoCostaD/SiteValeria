from django.contrib import admin

from .models import Categoria, Testemunho


class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Testemunho)
class TestemunhoAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'titulo', 'data_criacao', 'data_modificacao', 'publicado', 'categoria', 'autor', 'slug'
    ]

    list_display_links = 'id', 'titulo',

    search_fields = 'titulo', 'data_criacao', 'categoria', 'autor', 'publicado',

    list_filter = 'data_criacao', 'publicado', 'categoria', 'autor',

    list_per_page = 10

    list_editable = 'categoria', 'publicado',

    ordering = ['-id']

    prepopulated_fields = {
        "slug": ('titulo',)
    }


admin.site.register(Categoria, CategoriaAdmin)
