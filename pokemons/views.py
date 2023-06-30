from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Pokemon
import pandas as pd
import json
import os


               

def getPokemon(request):
    querySet = Pokemon.objects.all().values
    template = loader.get_template('pokemons.html')
    context = {
        'pokemons':querySet
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    pokemon= Pokemon.objects.get(id=id)
    template=loader.get_template('pokemon_details.html')
    context ={
        'pokemon':pokemon
    }
    return HttpResponse(template.render(context,request))

def importFromCSV(request):

    My_Path = os.path.dirname(__file__)
    csv_file_path = f'{My_Path}/data/pokemons.csv'
    dataframe=pd.read_csv(csv_file_path)
    dataframe=dataframe.tail(-1)
    dataframe.fillna('none')


    for pokemons in range(len(dataframe)):
        pokemon=Pokemon()

        pokemon.id=dataframe.iloc[pokemons]['id'] # save id field and record in database as id, same proccess for fallowing records
        pokemon.name=dataframe.iloc[pokemons]['name']
        pokemon.hp=dataframe.iloc[pokemons]['hp']
        types=dataframe.iloc[pokemons]['types'].replace("['","").replace("']","").replace("'","")  # remove brackets and colums as it don't need to save in data base
        pokemon.types=types
        abilities=str(dataframe.iloc[pokemons]['abilities'])
        #cut out from data description  of pockemon abilities, in case pokemon don't have ability record in data base that pokemon has no ability
        ability_start=abilities.find("'text'") 
        ability_end=abilities.find(", 'type'")
        if ability_start<0:
            ability_name="This pokemon doesn't have special ability!"
        else: ability_name=abilities[(ability_start+9) : (ability_end-1)]
        pokemon.abilities=ability_name
        #cut out from data description  of pockemon weaknesses, in case pokemon don't have weaknesses record in data base that pokemon has no weaknesses
        weaknesses=dataframe.iloc[pokemons]['weaknesses']
        weaknesses_start=weaknesses.find("'type':")
        weaknesses_end=weaknesses.find("', '")
        pokemon.weaknesses=weaknesses[(weaknesses_start+9): weaknesses_end]
        #cut out from data description  of pockemon resistances, in case pokemon don't have resistances record in data base that pokemon has no resistances
        resistances=str(dataframe.iloc[pokemons]['resistances'])
        resistances_start=resistances.find("'type':")
        resistances_end=resistances.find("', '")
        if resistances_start<0:
            resistan_type="This pokemon doesn't have resistance!"
        else: resistan_type=resistances[(resistances_start+9) : (resistances_end)]
        pokemon.resistances=resistan_type
        pokemon.convertedRetreatCost=dataframe.iloc[pokemons]['convertedRetreatCost']
        try: #make test if data exists, if no record as inpormation as unknown
            pokemon.artist=dataframe.iloc[pokemons]['artist']
        except: 
            pokemon.artist='Unknown'
        pokemon.rarity=dataframe.iloc[pokemons]['rarity']
        pokemon.flavorText=dataframe.iloc[pokemons]['flavorText']
        # split images record and store as small image and as big image
        image=dataframe.iloc[pokemons]['images'].split(',')
        large_image=image[1].split(':')
        large_image=large_image[2]
        small_image=image[0].split(':')
        small_image=small_image[2]
        pokemon.big_images=large_image[:-2]
        pokemon.small_images=small_image[:-1]
        pokemon.save() # save data in data base
        
    #display message about proccess is finished   
    return HttpResponse('Data records is done')
# Create your views here.
