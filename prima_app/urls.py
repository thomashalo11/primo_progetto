from django.urls import path
from prima_app.views import homepage, welcome, lista, chi_siamo, variabili

app_name="prima_app"
urlpatterns=[
    path('', homepage, name='homepage'),
    path('', welcome, name='welcome'),
    path('', lista, name='lista'),
    path('', chi_siamo, name="chi_siamo"),
    path('', variabili, name="variabili")
]