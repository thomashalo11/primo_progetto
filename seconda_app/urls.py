from django.urls import path
from seconda_app.views import es_if, index

app_name = "seconda_app"
urlpatterns=[

    path('', index, name='index'),
    path('es_if', es_if, name='es_if'),
]