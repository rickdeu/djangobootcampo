from django.contrib import admin
from core.models import *


class CategoriaAdmin(admin.ModelAdmin):
    ordering = ['nome_categoria']
    search_fields = ['nome_categoria']
    list_filter = ['nome_categoria']

class PerdidosAdmin(admin.ModelAdmin):
    ordering = ['date_registo', 'nomecompleto', 'bairro']
    list_display = ['id', 'nomecompleto', 'tipo_item', 'numero', 'bairro', 'declarante', 'data_perdido', 'date_registo']
    list_display_links = ['id', 'nomecompleto', 'tipo_item', 'numero', 'bairro', 'declarante', 'data_perdido', 'date_registo']
    search_fields = ['nomecompleto', 'numero', 'declarante', 'id']
    list_filter = ['tipo_item']
    autocomplete_fields = ['tipo_item']
    save_as = True




admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Perdidos, PerdidosAdmin)
admin.site.register(Achados)