from django.urls import path
from . import views

urlpatterns = [
    path('pokemons/import-data', views.importFromCSV, name='importData'),
    path('pokemons/pokemons', views.getPokemon, name='pokemons'),
    path('pokemons/pokemon_details/<slug:id>',views.details, name='pokemons'),
]