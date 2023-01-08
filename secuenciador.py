import random


def subcadenas(longitudSubcadena, numeroDeSubcadenas, cadena):  # Retorna una lista con subcadenas
    listaDeSubcadenas = []
    for x in range(numeroDeSubcadenas):
        rng = random.Random()
        indice = rng.randrange(0, len(cadena) - (longitudSubcadena - 1))
        subcadena = ""
        for y in range(longitudSubcadena):
            subcadena += cadena[indice + y]
        listaDeSubcadenas.append(subcadena)
    return listaDeSubcadenas


# Inicio de execucion

# Archivo con la longitud de las subcadenas
archivo1 = open("input.txt", "r")

# Archivo donde se van a escribir las subcadenas
archivo2 = open("subcadenas.txt", "w")
archivo3 = open("cadena.txt", "r")  # Archivo que tiene la cadena de ADN
cadena = archivo3.read()
longitudSubcadena = int(archivo1.readline().split()[3])
numeroDeSubcadenas = int(archivo1.readline().split()[4])

for subcadena in subcadenas(longitudSubcadena, numeroDeSubcadenas, cadena):
    archivo2.write(subcadena + "\n")

archivo3.close()
archivo2.close()
archivo1.close()
