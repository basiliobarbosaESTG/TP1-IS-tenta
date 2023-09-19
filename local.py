from ast import literal_eval
import json
import urllib.request
import csv

with open('Documents/athlete_events.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        city = row['City']


nameCity = input("Qual pais queres procurar? ")
response = urllib.request.urlopen('https://nominatim.openstreetmap.org/search?city=Lisbon&format=json')
dados = literal_eval(response.read().decode("utf-8"))
print(json.dumps(dados[0]['lat'], indent=2))
print(json.dumps(dados[0]['lon'], indent=2))
#print(json.dumps(dados, indent=2))