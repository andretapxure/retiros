
from django import forms
from .models import Participante, Retiro
 
 
# creating a form
class ParticipanteForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Participante
 
        # specify fields to be used
        fields = [
            "nome",
            "nascimento",
            "sexo",
            "estadocivil",
        ]


 
# creating a form
class RetiroForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Retiro
 
        # specify fields to be used
        fields = [
            "nome",
            "data",
            "descricao",
        ]        