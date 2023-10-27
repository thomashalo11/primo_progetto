app_name = "seconda_app"

from django.urls import path,include
from seconda_app.views import es_if

urlpatterns=[
    path('es_if',include("es_if.html", name='es_if')),
]