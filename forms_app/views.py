from django.shortcuts import render
from .forms import FormContatto
from django.http import HttpResponse

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