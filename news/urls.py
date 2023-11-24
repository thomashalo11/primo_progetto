from django.urls import path, include
from .views import home, homepage, articoloDetailView

app_name = 'news'

urlpatterns = [
    path('', home, name="homeview"),
    path('homepage', homepage, name="homepage"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
]
