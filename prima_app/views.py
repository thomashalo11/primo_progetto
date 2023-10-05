from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")
def variabili(request):
    context = {
        'var1': 'Prima variabile',
        'var2':  'Seconda variabile',
        'var3': 'Terza variabile'
    }
    return render(request, "variabili.html", context)