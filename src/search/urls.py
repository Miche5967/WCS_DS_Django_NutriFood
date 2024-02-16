from django.urls import path
# from .views import index # si on utilise cette ligne, alors il faut mettre uniquement views au lieu de views.index
from . import views

urlpatterns = [
    path('', views.index, name='search-index'),
]
