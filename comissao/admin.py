from django.contrib import admin
from comissao.models import *

# Register your models here.

class ClasseAdmin(admin.ModelAdmin):
    model = Classe
    list_display = ['numero', 'recrutas']


class NivelAdmin(admin.ModelAdmin):
    model = Nivel
    list_display = ['__unicode__', 'comissao', 'exp_minima']

admin.site.register(Classe, ClasseAdmin)
admin.site.register(Nivel, NivelAdmin)
# admin.site.register(Bonus)