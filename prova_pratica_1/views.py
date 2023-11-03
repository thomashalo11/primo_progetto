from django.shortcuts import render

# Create your views here.
def index_prova_pratica(request):
    return render(request, "index_prova_pratica.html")

def somma(request):
    return render(request, "somma.html") # Se poi aggiungo variabili in somma.html aggiungere un context

def media(request):
    return render(request, "media.html") # Se poi aggiungo variabili in media.html aggiungere un context

def voti(request):
    return render(request, "voti.html") # Se poi aggiungo variabili in voti.html aggiungere un context
