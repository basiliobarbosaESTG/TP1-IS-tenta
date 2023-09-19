from Converters.Classes.athlete_events import athlete_events
import csv

class converterXML:
    def __init__(self, file1, file2):
        self.athlete_events_file = file1
        self.name_file = file2

    #File
    def convert(self):
        try:
            def saveCSV(data):
                info = []
                for row in data:
                    info.append(row)
                return info 
            #ABERTURA DO FICHEIRO
            with open(self.athlete_events_file, 'r', encoding="UTF8") as file:
                reader = csv.reader(file, delimiter=',')
                next(reader)
                athletes = saveCSV(reader)
            
            #Escrever ficheiro xml (tentei mandar a saida do ficheiro para a pasta Documents)
            with open("Output\\"+self.name_file+".xml", "w", encoding="UTF8") as file:
                file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
                file.write("\t<athletes>\n")
                for a in athletes:
                    athlete =  athlete_events(a)
                    file.write(athlete.convert_toXML())
                file.write("\n\t</athletes>\n")

        except(Exception) as error:
            print("Error: ", error)         