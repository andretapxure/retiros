from django.contrib import admin
from .models import Participante, Retiro, Participacao
from csvexport.actions import csvexport
from decouple import config

admin.site.site_header = config("ADMIN_APP_NAME")

class ParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('retiro', 'participante')
    list_filter = ('retiro', 'participante')
    actions = [csvexport]

admin.site.register(Participacao, ParticipacaoAdmin)

class ParticipanteAdmin(admin.ModelAdmin):
    model = Participante
    list_display = ('nome', 'cpf', 'nascimento')
    list_filter = ('sexo', 'estadocivil')
    actions = [csvexport]

admin.site.register(Participante, ParticipanteAdmin)

class RetiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data')
    actions = [csvexport]

admin.site.register(Retiro, RetiroAdmin)

