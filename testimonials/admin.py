from django.contrib import admin

from .models import Category, Testimony


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    ...
