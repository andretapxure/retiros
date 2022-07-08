from django.contrib import admin
from .models import Participante, Retiro, Participacao

class ParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('retiro', 'participante')

admin.site.register(Participacao, ParticipacaoAdmin)

class ParticipanteAdmin(admin.ModelAdmin):
    model = Participante
    list_display = ('nome', 'cpf', 'nascimento')

admin.site.register(Participante, ParticipanteAdmin)

class RetiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data')

admin.site.register(Retiro, RetiroAdmin)

