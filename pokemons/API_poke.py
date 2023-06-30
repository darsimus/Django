import requests #allows you to send http requests using python
import json
import pandas as pd
import os
import csv

#set path to directory
My_Path = os.path.dirname(__file__) 
#set link to API
api_get=requests.get('https://api.pokemontcg.io/v2/cards')

#get data from api
x =json.loads(api_get.content)
data =[]
print(len(x["data"]))
for poke in x["data"]:
    data.append(poke)

'''Dict_keys(['id', 'name', 'supertype', 'subtypes', 'level', 'hp', 'types', 'evolvesFrom', 'abilities',
 'attacks', 'weaknesses', 'resistances', 'retreatCost', 'convertedRetreatCost', 'set', 'number', 'artist',
   'rarity', 'flavorText', 'nationalPokedexNumbers', 'legalities', 'images', 'tcgplayer', 'cardmarket'])'''

# list keys to delete
delete_keys=['legalities','regulationMark','rules', 'tcgplayer', 'cardmarket','supertype','level','subtypes','set', 'number','nationalPokedexNumbers','retreatCost','attacks', 'evolvesFrom', 'evolvesTo']#

#remove keys which is not planned to use
for x in data:
    for key in delete_keys:
        if key in x:
            x.pop(key)


# view key content
# for x in data:
#     argument='attacks'
#     if argument in x:
#         print(x[argument])

keys = data[0].keys() #asign keys to variable for futher using in csv file creation.

csv_file_path = f'{My_Path}/pokemons.csv' # make destanation path were to save csv file
#create csv file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys, delimiter=';')
    dict_writer.writeheader()
    dict_writer.writerows(data)

#create path to excel file
excel_file_path = f'{My_Path}/test.xlsx'

#tranfer csv file to excel file by using pandas library
df = pd.read_csv(csv_file_path)
df.to_excel(excel_file_path, index=False)

