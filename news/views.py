from django.shortcuts import render
from django.http import HttpResponse
from .models import Articolo, Giornalista
# Create your views here.

def home(request):
    """
    articolo = ""
    giornalista = ""
    for art in Articolo.objects.all():
        articolo += (art.titolo + "<br>")

    for gio in Giornalista.objects.all():
        giornalista += (gio.nome + "<br>")
    response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g

    return HttpResponse("<h1>Homepage news!</h1>")
    """

    """

    A differenza del primo creiamo degli array che contengono i vari articoli e giornalisti.
    Poi come risposta diamo il contenuto degli array trasformandoli in stringa.

    articolo = []
    giornalista = []
    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.nome)

    response = str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse("<h1>" + response + "</h1>")
    """
    """
    Rispetto alla versione precedente, passiamo direttamente ad articoli e giornalisti tutti gli oggetti (quindi gli articoli e i giornalisti rispettivamente)
    Nel context abbiamo gli articoli e i giornalisti che poi verranno printati.
    """
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli:": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage.html", context)