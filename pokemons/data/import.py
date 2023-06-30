import pandas as pd
import os
from models import Pokemon



My_Path = os.path.dirname(__file__)
csv_file_path = f'{My_Path}/pokemons.csv'

dataframe=pd.read_csv(csv_file_path)
dataframe=dataframe.tail(-1)

pokemon=Pokemon()

pokemon.id=dataframe.iloc[0]['id']
pokemon.name=dataframe.iloc[0]['name']
pokemon.hp=dataframe.iloc[0]['hp']
pokemon.types=dataframe.iloc[0]['types']
pokemon.abilities=dataframe.iloc[0]['abilities']
pokemon.weaknesses=dataframe.iloc[0]['weaknesses']
pokemon.resistances=dataframe.iloc[0]['resistances']
pokemon.convertedRetreatCost=dataframe.iloc[0]['convertedRetreatCost']
pokemon.artist=dataframe.iloc[0]['artist']
pokemon.rarity=dataframe.iloc[0]['rarity']
pokemon.flavorText=dataframe.iloc[0]['flavorText']
pokemon.images=dataframe.iloc[0]['images']



# dataframe = dataframe.iloc[0]['id'] 
# print(dataframe)
