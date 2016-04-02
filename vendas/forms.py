# coding=utf-8
from django import forms
from vendas.models import Pedido, ItensPedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        # widgets = {'data_referencia': forms.TextInput(attrs={'class': 'datepicker'}),
        #            'periodo_agenda_ini': forms.TextInput(attrs={'class': 'datepicker'}),
        #            'periodo_agenda_fim': forms.TextInput(attrs={'class': 'datepicker'}),
        #            'ativa': forms.CheckboxInput(attrs={'onclick': 'solicitacao_tooltipped()'})
        #           }

    # def clean(self):
    #     cleaned_data = super(AgendaCastracaoForm, self).clean()
    #
    #     if cleaned_data.get('periodo_agenda_fim') < cleaned_data.get('periodo_agenda_ini'):
    #         raise forms.ValidationError('O Inicio do Periodo de Agendamento tem que ser menor ou igual ao Fim do Periodo de Agendamento')
    #
    #     return cleaned_data



class ItensPedidoForm(forms.ModelForm):

    # referencia = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'browser-default', }), required=True)

    class Meta:
        model = ItensPedido
        fields = '__all__'
        # exclude = ['cliente', 'cpf_cliente', 'email_cliente', 'endereco_cliente']
        # widgets = {'data': forms.TextInput(attrs={'class': 'datepicker'}),}

    # def clean(self):
    #     cleaned_data = super(AgendaCastracaoItensForm, self).clean()
    #     if not cleaned_data['DELETE']:
    #         if all(name in cleaned_data for name in ['machos', 'femea_felino', 'femea_Canino']) and (cleaned_data['machos']+cleaned_data['femea_felino']+cleaned_data['femea_Canino']) <= 0:
    #             raise forms.ValidationError("Na data %s ao menos um dos campos Machos, Fêmea Felino ou Fêmea Canino tem que ser maior que 0" %(cleaned_data['data'].strftime("%d/%m/%Y") if 'data' in cleaned_data else ''))
    #
    #         if cleaned_data['agenda'].id and (cleaned_data['agenda'].data_referencia.month != cleaned_data['data'].month or cleaned_data['agenda'].data_referencia.year != cleaned_data['data'].year):
    #             self._errors['data'] = 'Data fora da referencia'
    #             raise forms.ValidationError('A data %s esta fora da referencia' % (cleaned_data['data'].strftime("%d/%m/%Y")))
    #
    #     return cleaned_data
