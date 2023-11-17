from django.urls import path, include
from .views import home, homepage

app_name = 'news'

urlpatterns = [
    path('', home, name="homeview"),
    path('homepage', homepage, name="homepage"),
]
