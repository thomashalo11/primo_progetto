from django.contrib import admin
from django.urls import path, include
from .views import contatti, visualizza_contatti

app_name = 'forms_app'

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path('visualizza_contatti/', visualizza_contatti, name='visualizza_contatti') # Eliminare se ci sono problemi
]
