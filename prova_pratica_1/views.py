import random
from django.shortcuts import render

# Create your views here.
def index_prova_pratica(request):
    return render(request, "index_prova_pratica.html")

def somma(request):
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    nSomma = num1 + num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'nSomma' : nSomma,
    }
    return render(request, "somma.html", context) # Se poi aggiungo variabili in somma.html aggiungere un context

def media(request):
    numeri = []
    n = 30
    somma = 0
    # Creazione lista
    for i in range(n):
        numeri.append(random.randint(1,10))
    # Somma
    for i in range(len(numeri)):
        somma += numeri[i]
    # Media
    media = somma / len(numeri)
    
    context = {
        'numeri' : numeri,
        'somma' : somma,
        'media' : media,
    }
    return render(request, "media.html", context) # Se poi aggiungo variabili in media.html aggiungere un context

def voti(request):
    context = {
        'voto' : {"studente1":8, "studente2":7,"studente3":5}
    }
    return render(request, "voti.html", context) # Se poi aggiungo variabili in voti.html aggiungere un context
