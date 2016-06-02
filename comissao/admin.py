from django.contrib import admin
from comissao.models import *

# Register your models here.
class NivelInlineAdmin(admin.TabularInline):
    model = Nivel
    extra = 0
    min_num = 1

class ClasseAdmin(admin.ModelAdmin):
    model = Classe
    list_display = ['numero', 'recrutas', 'exp_minima']
    inlines = [NivelInlineAdmin]


class NivelAdmin(admin.ModelAdmin):
    model = Nivel
    list_display = ['__unicode__', 'comissao', 'exp_minima']


class PeriodoComissaoAdmin(admin.ModelAdmin):
    model = PeriodoComissao
    list_display = ['__unicode__', 'inicio_periodo', 'fim_periodo']

admin.site.register(Classe, ClasseAdmin)
admin.site.register(Nivel, NivelAdmin)
admin.site.register(PeriodoComissao, PeriodoComissaoAdmin)
# admin.site.register(Bonus)