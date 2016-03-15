from django.contrib import admin
from vendas.models import *
# Register your models here.


class ItensPedidoInlineAdmin(admin.TabularInline):
    model = ItensPedido


class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    inlines = [ItensPedidoInlineAdmin]


admin.site.register(Pedido, PedidoAdmin)