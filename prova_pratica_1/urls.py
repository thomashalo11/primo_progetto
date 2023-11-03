from django.urls import path
from prova_pratica_1.views import index_prova_pratica, somma, media, voti

app_name = "prova_pratica_1"
urlpatterns = [
    path('index_prova_pratica', index_prova_pratica, name='index'),
    path('somma', somma, name='somma'),
    path('media', media, name='media'),
    path('voti', voti, name='voti')
]