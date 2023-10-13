from django.shortcuts import render

# Create your views here.

def index_root(request):
    return render(request, "index_root.html")
def index(request):
    return render(request, "index.html")
def homepage(request):
    return render(request, "homepage.html")
def welcome(request):
    return render(request, "welcome.html")
def lista(request):
    return render(request, "lista.html")
def chi_siamo(request):
    return render(request, "chisiamo.html")
def variabili(request):
    return render(request, "variabili.html")

def variabili(request):
    context = {
        'var1': 'Prima variabile',
        'var2': 'Seconda variabile',
        'var3': 'Terza variabile'
    }
    return render(request, "variabili.html", context)