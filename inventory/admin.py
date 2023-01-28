from django.contrib import admin
from inventory.models import Inventory

class ListandoInventory(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'quantidade', 'preco')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_editable = ('quantidade', )

admin.site.register(Inventory, ListandoInventory)