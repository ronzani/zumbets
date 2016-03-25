# coding=utf-8
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.forms import inlineformset_factory
from django.views.generic import ListView

import distribuidor
from vendas.forms import PedidoForm, ItensPedidoForm
from vendas.models import Pedido, ItensPedido



class PedidosList(ListView):
    model = Pedido
    template_name = 'pedido_list.html'
    form_class = PedidoForm
    paginate_by = 10
    paginate_orphans = 5

    # def get_paginator(self, queryset, per_page, orphans=5, allow_empty_first_page=True, **kwargs):
    #     paginator = DiggPaginator(queryset, per_page, body=9, padding=4)
    #     return paginator

    def get_queryset(self):
        pedidos = Pedido.objects.all()
        var_get_search = self.request.GET.get('search_box')

        if var_get_search is not None:
            pedidos = pedidos.filter(Q(distribuidor__first_name__icontains=var_get_search)|
                                     Q(distribuidor__last_name__icontains=var_get_search))
        return pedidos


def pedido_add(request):
    msg = []

    itens_pedidoInlineFormSet = inlineformset_factory(Pedido, ItensPedido,
                                                      ItensPedidoForm, can_delete=True, extra=0, min_num=1)

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        formset = itens_pedidoInlineFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    pedido = form.save()
                    for f in formset:
                        if not f.cleaned_data['DELETE']:
                            item = f.save(commit=False)
                            item.pedido = pedido
                            item.save()
                    return HttpResponseRedirect('')
            except Exception, e:
                msg = e

    else:
        form = PedidoForm
        formset = itens_pedidoInlineFormSet
    return render(request, 'pedido_form.html', {
        'form': form,
        'formset': formset,
        'titulo': 'Pedido de Venda',
        'erro': msg
    })


def pedidos_up(request, pk):
    warning = None
    msg = []
    pedido = get_object_or_404(Pedido, pk=pk)

    itens_pedidoInlineFormSet = inlineformset_factory(Pedido, ItensPedido,
                                                      ItensPedidoForm, can_delete=True, extra=0, min_num=1)

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        formset = itens_pedidoInlineFormSet(request.POST, instance=pedido)
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    formset.save()
                    return HttpResponseRedirect('')
            except Exception, e:
                msg = e
    else:
        form = PedidoForm(instance=pedido)
        formset = itens_pedidoInlineFormSet(instance=pedido)
    return render(request, '', {
        'form': form,
        'formset': formset,
        'titulo': 'Editar Pedido de Venda',
        'erro': msg,
        'warning': warning
    })