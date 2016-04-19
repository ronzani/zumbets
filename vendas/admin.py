from django.contrib import admin
from vendas.models import *
from vendas.forms import ItensPedidoForm, PedidoForm
# Register your models here.


class ItensPedidoInlineAdmin(admin.TabularInline):
    model = ItensPedido
    form = ItensPedidoForm


class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    form = PedidoForm
    inlines = [ItensPedidoInlineAdmin]


admin.site.register(Pedido, PedidoAdmin)