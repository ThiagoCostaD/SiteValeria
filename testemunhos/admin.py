from django.contrib import admin
from .models import Categoria, Testemunho


class CategoriaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Categoria, CategoriaAdmin)


@admin.register(Testemunho)
class TestemunhoAdmin(admin.ModelAdmin):
    ...
