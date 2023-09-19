from xmlrpc.server import SimpleXMLRPCServer
from psycopg2 import Error
import datetime,json,psycopg2
from Database import querys
from Converters.xml_related.converterXML import converterXML
from Converters.xml_related.validatorXML import validateXML

f = open('config.json')
data = json.load(f).get('dbconfig')
connection = psycopg2.connect(
    host=data.get('host'),
    port=data.get('port'), 
    user=data.get('user'),
    password=data.get('password'),  
    database=data.get('database')) #Conecção a base de dados

cursor = connection.cursor()

# print("PostgreSQL server information")
# print(connection.get_dsn_parameters(), "\n")

cursor.execute("SELECT version();") #Verifcar coneção
record = cursor.fetchone()
print("You are connected to - ", record, "\n")

def convert(athlete_events_file,name_file): #Chama a classe que faz a conversao do ficheiro de CSV para XML
    c = converterXML(athlete_events_file,name_file)
    result = c.convert()
    print(result)

def validate(xml, xsd): #Chama a classe que faz a validação do XML com o XSD
    return validateXML(xml, xsd)

def get_date(): #Retorna a data atual
    return datetime.datetime.now()

def insert_file(name, file): #INSERIR FICHEIRO NA BD
    insert_data = (name, file, get_date())
    try:
        cursor.execute(querys.insert_sp, insert_data)
        connection.commit()
        cursor.execute(querys.get_last)
        result = cursor.fetchall()
        print("File saved\n")
        return str(result)
    except (Exception, Error) as error:
        connection.rollback()
        print("Error inserting new file", error)
        return(str(error))
        
def deleteFile(id): #Delete FICHEIRO
    try:
        cursor.execute(querys.delete_sp, [id])
        connection.commit()
        cursor.execute(querys.get_row, [id])
        result = cursor.fetchall()
        print(result)
        print("File deleted\n Outout: " + str(result))
        return str(result)
    except (Exception, Error) as error:
        connection.rollback()
        print("Error deleting file", error)
        return(str(error))

#CONSULTAS
#PEDIDO A BD PARA EXECUTAR O SEGUINT XPATH/XQUERY QUE OBTEM OS DADOS DE UM ATLETA A PARTIR DO SEU NOME
#/*/ todo que esta dentro do athelte do atribyuto name
def getAthleteByName(name, id): #, id - name,sex
    try:
        cursor.execute("SELECT unnest(CAST(XPATH('/athletes/atlethe[@name=\""+name+"\"]/@name', xml)AS TEXT)::text[]) AS nome, unnest(CAST(xpath('/athletes/atlethe[@name=\""+name+"\"]/sex/text()', xml)AS TEXT)::text[]) AS sexo, unnest(CAST(xpath('/athletes/atlethe[@name=\""+name+"\"]/age/text()', xml)AS TEXT)::text[]) AS idade FROM xmldata where id="+id)
        #cursor.execute("SELECT unnest(xpath('/athletes/atlethe[@name=\""+name+"\"]/sex/text()', xml)) AS sexo FROM xmldata where id="+id)
        connection.commit()
        result = cursor.fetchall()
        print(len(result))
        #print(type(result[0]))
        print(type(result)) 
        #Type serve para ver o tipo de dado da variavel
        return result
    except (Exception, Error) as error:
        connection.rollback()
        print("Error executing: ", error)
        return(str(error))

#Consulta conta quantas medalhas existem de cada tipo
def getGroupByMedlas(id):
    try:
        cursor.execute("SELECT unnest(cast(xpath('/athletes/atlethe/competition/statsBySport/medal/text()', xml)as TEXT)::text[]) as medalhas, count(*) as contagem FROM xmldata where id="+id+" group by medalhas") 
        connection.commit()
        result = cursor.fetchall()
        print(len(result))
        print(type(result))
        return result
    except (Exception, Error) as error:
        connection.rollback()
        print("Error executing: ", error)
        return(str(error))

#Consulta conta quantas medalhas existem de cada tipo
def getGroupBySport(id):
    try:
        cursor.execute("SELECT unnest(cast(xpath('/athletes/atlethe/competition/statsBySport/sport/text()', xml)as TEXT)::text[]) as desporto, count(*) as contagem FROM xmldata where id="+id+" group by desporto") 
        connection.commit()
        result = cursor.fetchall()
        print(len(result))
        print(type(result))
        return result
    except (Exception, Error) as error:
        connection.rollback()
        print("Error executing: ", error)
        return(str(error))

#Consulta conta quantas medalhas existem de cada tipo
def getGroupBySex(id):
    try:
        cursor.execute("SELECT unnest(cast(xpath('/athletes/atlethe/sex/text()', xml)as TEXT)::text[]) as sex, count(*) as contagem FROM xmldata where id="+id+" group by sex order by contagem asc") 
        connection.commit()
        result = cursor.fetchall()
        print(len(result))
        print(type(result))
        return result
    except (Exception, Error) as error:
        connection.rollback()
        print("Error executing: ", error)
        return(str(error))

def getSportByName(name, id):
    try:
        cursor.execute("SELECT unnest(cast(xpath('/athletes/atlethe[@name=\""+name+"\"]/competition/statsBySport/sport/text()', xml)as TEXT)::text[]) as desporto FROM xmldata where id="+id) 
        connection.commit()
        result = cursor.fetchall()
        print(len(result))
        print(type(result))
        return result
    except (Exception, Error) as error:
        connection.rollback()
        print("Error executing: ", error)
        return(str(error))

def getEventByName(name, id):
    try:
        cursor.execute("SELECT unnest(cast(xpath('/athletes/atlethe[@name=\""+name+"\"]/competition/statsBySport/event/text()', xml)as TEXT)::text[]) as evento FROM xmldata where id="+id) 
        connection.commit()
        result = cursor.fetchall()
        print(len(result))
        print(type(result))
        return result
    except (Exception, Error) as error:
        connection.rollback()
        print("Error executing: ", error)
        return(str(error))

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Listening on port 8000...")

#REGISTO DAS FUNÇOES
server.register_function(convert, "convert")
server.register_function(validate, "validate")
server.register_function(insert_file, "insert_file")
server.register_function(getAthleteByName, "getAthleteByName")
server.register_function(getGroupByMedlas, "getGroupByMedlas")
server.register_function(getGroupBySport, "getGroupBySport")
server.register_function(getGroupBySex, "getGroupBySex")
server.register_function(getSportByName, "getSportByName")
server.register_function(getEventByName, "getEventByName")
server.register_function(deleteFile, "delete_file")

server.serve_forever()