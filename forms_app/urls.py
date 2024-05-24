from django.contrib import admin
from django.urls import path, include
from .views import contatti, visualizza_contatti, modifica_contatti, elimina_contatti

app_name = 'forms_app'

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path('visualizza_contatti/', visualizza_contatti, name='visualizza_contatti'), # Eliminare se ci sono problemi
    path('modifica_contatti/<int:pk>/', modifica_contatti, name='modifica_contatti'), # Eliminare se ci sono problemi
    path('elimina_contatti/<int:pk>/', elimina_contatti, name='elimina_contatti'), # Eliminare se ci sono problemi
]
