from django.contrib import admin
from galeria.models import Fotografia

class ListaFotografias(admin.ModelAdmin):
    list_display = ["id", "nome", "legenda", "publicada", "data_fotografia"]
    list_display_links = ["id", "nome"]
    list_editable = ["publicada"]
    search_fields = ["nome"]
    list_filter = ["categoria"]
    list_per_page = 10

admin.site.register(Fotografia, ListaFotografias)
