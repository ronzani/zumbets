from django.conf.urls import patterns, url
from vendas.views import PedidosList


urlpatterns = patterns('',
                       url(r'^pedidos/$', PedidosList.as_view(), name='pedidos_list'),
                       url(r'^pedidos/add/$', 'vendas.views.pedido_add', name='pedidos_add'),
                       url(r'^pedidos/(?P<pk>\d+)/$', 'vendas.views.pedidos_up', name='pedidos_up'),
                       )