from datetime import datetime

def getTextFile(FileName):
    fileReader = open(FileName, "r")

    file = ""
    for row in fileReader:
        file +=row

    return(file)


def replasePhase(texto,fraseReplace):
    print("Reemplaze " + fraseReplace)
    UserInput = input();
    return texto.replace(fraseReplace,UserInput)

contrato = getTextFile("contrato.txt")


# contrato =contrato.replace("[EMPLOYEE_NAME]", "Programador Junior")
# contrato =contrato.replace("[CITY]", "Puno")
# contrato =contrato.replace("[COUNTRY]", "Perú")

contrato = replasePhase(contrato, "[COMPANY_NAME]")
contrato = replasePhase(contrato, "[EMPLOYEE_NAME]")
contrato = replasePhase(contrato, "[CITY]")
contrato = replasePhase(contrato, "[COUNTRY]")

fecha_hoy= datetime.today().strftime('%d/%m/%Y')  # da lo mismo / o - se convereteen caracter
contrato =contrato.replace("[CURRENT_DATE]", fecha_hoy)


print(contrato)

with open("Contrato_new.txt", "w") as file:
    file.write(contrato)