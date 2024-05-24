from django.shortcuts import render
from .forms import FormContatto
from django.http import HttpResponse
from .models import Contatto
from django.shortcuts import get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

# Create your views here.
"""
def contatti(request):
    form = FormContatto()
    context = {"form": form}
    return render(request, "contatto.html", context)
"""
def contatti(request):
    if request.method == "POST":
        form = FormContatto(request.POST)
        
        if form.is_valid():
            print("Il form è valido")
            print("Nome: ", form.cleaned_data["nome"])
            print("Cognome: ", form.cleaned_data["cognome"])
            print("Email: ", form.cleaned_data["email"])
            print("Contenuto: ", form.cleaned_data["contenuto"])
            print("Salvataggio contatto...")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)            
            return HttpResponse("<h1>Grazie per averci contattato :)</h1>")
    else:
        form = FormContatto()
        
    context = {"form": form}
    return render(request, "contatto.html", context)

def visualizza_contatti(request):
    contatti = Contatto.objects.all()
    return render(request, 'visualizza_contatti.html', {'contatti': contatti})

@login_required(login_url="/accounts/login")
def modifica_contatti(request, pk):
    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "GET":
        form = FormContatto(instance=contatto)
    if request.method == "POST":
        form = FormContatto(request.POST, instance=contatto)
        if form.is_valid():
            form.save()
            return redirect('forms_app:visualizza_contatti')

    context = {'form': form, 'contatto': contatto}
    return render(request, 'modifica_contatti.html', context)

@staff_member_required(login_url="/accounts/login")
def elimina_contatti(request, pk):
    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "POST":
        contatto.delete()
        return redirect('forms_app:visualizza_contatti')
    context = {'contatto': contatto}
    return render(request, 'elimina_contatti.html', context)