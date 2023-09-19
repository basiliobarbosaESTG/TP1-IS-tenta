import xmlschema

def validateXML(xml_path, xsd_path): #FAZ A VALIDAÇÃO DO XML REOTRNADO VERDADEIRO OU FALSO
    try:
        my_schema = xmlschema.XMLSchema(xsd_path)
        if my_schema.is_valid(xml_path):
            return "File is valid!"
        else:
            return "File is not valid with this xsd"
    except(Exception) as error:
        return "Error while validating the XML file: " + str(error)