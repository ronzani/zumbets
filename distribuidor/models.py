# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

from comissao.models import Nivel
from vendas.models import Pedido


CHOICES_SEXO = (('m', 'Masculino'),
                ('f', 'Feminino'),
                )

CHOICES_UNIDADE_FEDERATIVA = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AM', 'Amazonas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraiba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergige'),
    ('TO', 'Tocantins'),
)

class Pessoa(User):
    cpf = models.CharField(max_length=11, verbose_name='CPF', unique=True)
    data_nascimento = models.DateField(verbose_name='Data Nascimento')
    sexo = models.CharField(max_length=1, verbose_name='Sexo', choices=CHOICES_SEXO)
    rg = models.CharField(max_length=30, verbose_name='RG')
    orgao_emissor = models.CharField(max_length=30, verbose_name='Orgão Emissor')
    estado = models.CharField(max_length=2, verbose_name='Estado', choices=CHOICES_UNIDADE_FEDERATIVA)
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    cep = models.PositiveIntegerField(verbose_name='CEP')
    endereco = models.CharField(max_length=100, verbose_name='Endereço')
    telefone1 = models.CharField(max_length=16, verbose_name='Telefone1')
    telefone2 = models.CharField(max_length=16, verbose_name='Telefone2', blank=True, null=True)
    # nivel = models.ForeignKey('comissao.Nivel', verbose_name='Nivel')
    classe = models.ForeignKey('comissao.Classe', verbose_name='Classe')
    recrutador = models.ForeignKey('distribuidor.Pessoa', verbose_name='Recrutador', null=True, blank=True)
    exp = models.BigIntegerField(verbose_name='Experiência')

    def __unicode__(self):
        return '%s' % self.get_full_name()

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def set_exp(self, exp):
        self.exp = self.exp + exp
        self.save()

    def calcula_comissao(self):

        vendas = Pedido.objects.filter(distribuidor=self.id, status=3)
        vendas_diretas = 0

        for venda in vendas:
            vendas_diretas += venda.get_preco_pedido()

        per_comissao_direta = Nivel.objects.filter(classe=self.classe,
                                                   exp_minima__lte=vendas_diretas,
                                                   exp_maxima__gte=vendas_diretas).first().comissao

        comissao_venda_direta = float(vendas_diretas*per_comissao_direta/100)

        return comissao_venda_direta


def validate_cpf(cpf):
    cpf_invalidos = [11 * str(i) for i in range(10)]
    if cpf in cpf_invalidos:
        return False

    if not cpf.isdigit():
        """ Verifica se o CPF contem pontos e hifens """
        cpf = cpf.replace('.', '').replace('-', '')

    if len(cpf) < 11:
        """ Verifica se o CPF tem 11 digitos """
        return False

    if len(cpf) > 11:
        """ CPF tem que ter 11 digitos """
        return False

    selfcpf = [int(x) for x in cpf]

    cpf = selfcpf[:9]

    while len(cpf) < 11:

        r = sum([(len(cpf) + 1 - i) * v for i, v in [(x, cpf[x]) for x in range(len(cpf))]]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        cpf.append(f)

    return bool(cpf == selfcpf)
