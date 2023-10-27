from django.urls import path
from seconda_app.views import es_if, index2

app_name = "seconda_app"
urlpatterns=[

    path('index', index2, name='index2'),
    path('es_if', es_if, name='es_if'),
]