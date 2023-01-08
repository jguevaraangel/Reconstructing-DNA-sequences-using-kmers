import random


def cadenaDeADN(longitudCadena, cadena, basesNitrogenadas):
    # Retorna una cadena de ADN aleatoria
    for i in range(longitudCadena):
        cadena += random.choice(basesNitrogenadas)
    return cadena


# Inicio de la ejecución

# Archivo donde se va a escribir la cadena de ADN
archivo1 = open("cadena.txt", "w")

# Archivo que tiene la longitud de la cadena de ADN
archivo2 = open("longitudCadena.txt", "r")
longitudCadena = int(archivo2.readline().split()[5])

# Lista con las bases nitrogenadas de una molecula de ADN
basesNitrogenadas = ["A", "T", "C", "G"]
cadena = ""

archivo1.write(cadenaDeADN(longitudCadena, cadena, basesNitrogenadas))
archivo2.close()
archivo1.close()
