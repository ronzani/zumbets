# coding=utf-8
from django import forms
from vendas.models import Pedido, ItensPedido
from produto.models import Estoque


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        # widgets = {'data_referencia': forms.TextInput(attrs={'class': 'datepicker'}),
        #            'periodo_agenda_ini': forms.TextInput(attrs={'class': 'datepicker'}),
        #            'periodo_agenda_fim': forms.TextInput(attrs={'class': 'datepicker'}),
        #            'ativa': forms.CheckboxInput(attrs={'onclick': 'solicitacao_tooltipped()'})
        #           }

    def clean(self):
        cleaned_data = super(PedidoForm, self).clean()
        status = cleaned_data.get('status')
        pedido = Pedido.objects.filter(id=self.instance.id).first()

        if pedido:
            if pedido.status == '1':
                if status == '1':
                    self._errors['status'] = 'O status do pedido deve ser alterado.'
            elif pedido.status == '2':
                if status in ['1', '2']:
                    self._errors['status'] = 'O pedido deve ser alterado para concluido ou cancelado.'
            elif pedido.status == '3':
                self._errors['status'] = u'Após o pedido concluido, não é possivel altera-lo.'
            else:
                self._errors['status'] = u'Após o pedido cancelado, não é possivel altera-lo.'
        else:
            if not status == '1':
                self._errors['status'] = 'O pedido tem que ser aberto no status Aguardando Pagamento.'
        return cleaned_data



class ItensPedidoForm(forms.ModelForm):

    # referencia = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'browser-default', }), required=True)

    class Meta:
        model = ItensPedido
        fields = '__all__'
        exclude = ['cliente', 'cpf_cliente', 'email_cliente', 'endereco_cliente']
        # widgets = {'data': forms.TextInput(attrs={'class': 'datepicker'}),}

    def clean(self):
        cleaned_data = super(ItensPedidoForm, self).clean()
        camiseta = cleaned_data.get('camiseta')
        if not cleaned_data['DELETE']:
            estoque = Estoque.objects.filter(camiseta=camiseta).first()
            if estoque:
                if cleaned_data.get('quantidade') > estoque.get_quantidade_disponivel():
                    self._errors['quantidade'] = u'Quantidade indisponível em Estoque'
                    raise forms.ValidationError(u'Não há quantidade suficiente em estoque da camiseta %s' % camiseta)
            else:
                self._errors['camiseta'] = u'Não há entrada de estoque para esta camiseta.'
                raise forms.ValidationError(u'Não há entrada de estoque para a camiseta %s' %camiseta)
        return cleaned_data
