from django.shortcuts import render
 
# relative import of forms
from .models import Participante, Retiro
from .forms import ParticipanteForm, RetiroForm
 
 
def create_view_participante(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ParticipanteForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view_participante.html", context)

def create_view_retiro(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = RetiroForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view_retiro.html", context)    