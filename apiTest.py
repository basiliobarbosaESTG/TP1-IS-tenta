import requests
import csv

#def buscar_dados(self, line_csv):
#        nameCity = input("Qual pais queres procurar? ")
#        self.city = line_csv[11]
#        print(self.city)
#        city = self.city
#        response = requests.get("https://nominatim.openstreetmap.org/search?city=Lisbon&format=json") #ou /json  Lisbon

#        data = response.json()

#        print(type(data))

#        print(response.status_code)
#        print(data)

#        for coordenates in data:
#                #print(type(lat))
#                print(coordenates['lat'], coordenates['lon'])

#if __name__ == '__main__':
#    buscar_dados(self=a, line_csv=)

with open('Documents/athlete_events.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    #print(reader)
    #print(list(reader))
    var = list(reader)
    #for row in reader:
    for i in range(0,10):
        city = var[i]['City']
        #city = row['City']
        #print(row, city)

        response = requests.get(f"https://nominatim.openstreetmap.org/search?city={city}&format=json") #ou /json  Lisbon
        #print(city)

        data = response.json()
        #print(data)
        print(type(data))

        print(f"A cidade e: {city}")
        print(data[0]['lat'])
        print(data[0]['lon'])


        #for value in data:
                #print(value)

        #print(response.status_code)
        #print(data)

        #for coordenates in data:
                #print(type(lat))
                #print("A cidade é "+city+", tem uma latitude de "+coordenates['lat']+ ", tem uma longitude de " +coordenates['lon'])