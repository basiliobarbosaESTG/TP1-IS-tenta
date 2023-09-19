import xmlrpc.client

def conect_rpc():
    conn = xmlrpc.client.ServerProxy("http://localhost:8000/")
    return conn

def convert_():
    athlete_events_file = input("Insert athlete_events_file: ")
    name_file = input("Insert name: ")
    try:
        conn = conect_rpc()
        conn.convert(athlete_events_file, name_file)
        return name_file + ".xml"
    except(Exception) as error:
        print("Error: ", error)

def validate():
    xml = input("Insert XML file: ")
    xsd = input("Insert XSD file: ")
    try:
        conn = conect_rpc()
        print(conn.validate(xml, xsd))
    except(Exception) as error:
        print("Error: ", error)

def insert_doc():
    try:
        name = input("Insert a name: ")
        file = input("Insert the file: ")
        conn = conect_rpc()
        ficheiro = open(file, encoding="UTF8").read()
        result = conn.insert_file(name, ficheiro)
        print("Output: " + str(result))
    except(Exception) as error:
        print("Error: ", error)

def getAthleteByName():
    try:
        #sex = input("Insert the athelete sex: \n EX: M\n")
        name = input("Insert the athelete name: \n EX: A Lamusi\n")
        id = input("Insert the id of de row: ")
        conn = conect_rpc()
        result = conn.getAthleteByName(name, id) #, id - name, sex
        #print("Athele Info:\n\tName: "+ result[0][1]+ "\n\tSex: " + result[0][2])
        #for r in result:
        print(result[0]) # print("Athele Info:\n\tName: "+ r[0]) ->   [1][0] + "\n\tSex: " + result[2][0] + "\n\tAge: "+ result[3][0]
    except(Exception) as error:
        print("Error: ", error)

def getGroupByMedlas():
    try:
        id = input("Insert the id of de row: ")
        conn = conect_rpc()
        result = conn.getGroupByMedlas(id)
        for r in result:
            print(r)
    except(Exception) as error:
        print("Error: ", error)

def getGroupBySport():
    try:
        id = input("Insert the id of de row: ")
        conn = conect_rpc()
        result = conn.getGroupBySport(id)
        for r in result:
            print(r)
    except(Exception) as error:
        print("Error: ", error)

def getGroupBySex():
    try:
        id = input("Insert the id of de row: ")
        conn = conect_rpc()
        result = conn.getGroupBySex(id)
        for r in result:
            print(r)
    except(Exception) as error:
        print("Error: ", error)

def getSportByName():
    try:
        name = input("Insert the athelete name: \n EX: A Lamusi\n")
        id = input("Insert the id of de row: ")
        conn = conect_rpc()
        result = conn.getSportByName(name, id)
        for r in result:
            print(r)
    except(Exception) as error:
        print("Error: ", error)

def getEventByName():
    try:
        name = input("Insert the athelete name: \n EX: A Lamusi\n")
        id = input("Insert the id of de row: ")
        conn = conect_rpc()
        result = conn.getEventByName(name, id)
        for r in result:
            print(r)
    except(Exception) as error:
        print("Error: ", error)

#OPCAO 10
def softDelete():
    id = input("Insert the ID: ")
    try:
        conn = conect_rpc()
        result = conn.delete_file(id)
        print("Output: " + str(result))
    except(Exception) as error:
        print("Error: ", error)

def menu():
    while True:
        print("1 - Convert CSV to XML")
        print("2 - Validate XML with Schemma")
        print("3 - Insert XML Document on Database")
        print("4 - Get Athlete by name")
        print("5 - Get Group By Medals")
        print("6 - Get Group By Sport")
        print("7 - Get Group By Sex")
        print("8 - Get Sport By Name of Athlete")
        print("9 - Get Event By Name of Athlete")
        print("10 - Soft Delete")
        print("0 - Quit")
        escolha = input("Choose a option: ")
        if escolha == "1":
            convert_()
        if escolha == "2":
            validate()
        if escolha == "3":
            insert_doc()
        if escolha == "4":
            getAthleteByName()
        if escolha == "5":
            getGroupByMedlas()
        if escolha == "6":
            getGroupBySport()
        if escolha == "7":
            getGroupBySex()
        if escolha == "8":
            getSportByName()
        if escolha == "9":
            getEventByName()
        #OPCAO 10
        if escolha == "10":
            softDelete()
        if escolha == "0":
            print("Bye")
            quit()

def main():
    menu()

if __name__ == "__main__":
    main()