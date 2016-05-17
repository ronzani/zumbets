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


# class HospitalRegistrationForm(forms.Form):
#     class EmergencyContractForm(forms.Form):
#         name = forms.CharField()
#         relationship = forms.ChoiceField(choices=(
#             ('SPS', 'Spouse'), ('PRT', 'Partner'),
#             ('FRD', 'Friend'), ('CLG', 'Colleague')))
#         daytime_phone = forms.CharField()
#         evening_phone = forms.CharField(required=False)
#
#     registration_date = forms.DateField(initial=datetime.date.today)
#     full_name = forms.CharField()
#     birth_date = forms.DateField()
#     height = forms.IntegerField(help_text='cm')
#     weight = forms.IntegerField(help_text='kg')
#     primary_care_physician = forms.CharField()
#     date_of_last_appointment = forms.DateField()
#     home_phone = forms.CharField()
#     work_phone = forms.CharField(required=False)
#
#     procedural_questions = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple, required=False,
#         choices=QUESTION_CHOICES)
#
#     cardiovascular_risks = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple, required=False,
#         choices=CARDIOVASCULAR_RISK_CHOICES)
#
#     apnia_risks = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple, required=False,
#         choices=APNIA_RISK_CHOICES)
#
#     emergency_contacts = FormSetField(formset_factory(EmergencyContractForm, extra=2, can_delete=True))
#
#     layout = Layout(Row(Column('full_name',
#                                'birth_date',
#                                Row('height', 'weight'),
#                                span_columns=3),
#                         'registration_date'),
#
#                     Row(Span3('primary_care_physician'), 'date_of_last_appointment'),
#                     Row('home_phone', 'work_phone'),
#                     Fieldset('Procedural Questions', 'procedural_questions'),
#                     Fieldset('Clinical Predictores of Cardiovascular Risk', 'cardiovascular_risks'),
#                     Fieldset('Clinical Predictors of sleep Apnia Risk', 'apnia_risks'),
#                     Fieldset('Emergence Numbers', 'emergency_contacts')
#                     )