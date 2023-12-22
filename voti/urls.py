from django.urls import path
from voti.views import index3, view_a, view_b, view_c

app_name = "voti"

urlpatterns = [
    path('index3', index3, name="index3"),
    path('view_a', view_a, name="lista_materie"),
    path('view_b', view_b, name="voti_e_assenze"),
    path('view_c', view_c, name="media_voti_studenti"),
]