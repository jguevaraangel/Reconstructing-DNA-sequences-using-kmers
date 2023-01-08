import secuenciaDeADN
import secuenciador
import ensamblador
import numpy as np
import matplotlib.pyplot as plt


def indiceDeSimilaridad(longitudCadena, longitudSubcadena, numSubcadenas, longitudK):
    cadena = ""
    basesNitrogenadas = ["A", "T", "C", "G"]

    cadena = secuenciaDeADN.cadenaDeADN(
        longitudCadena, cadena, basesNitrogenadas)
    subcadenas = secuenciador.subcads(longitudSubcadena, numSubcadenas, cadena)
    kmers = ensamblador.kmer_list(subcadenas, longitudSubcadena, longitudK)
    indice = ensamblador.assembler(kmers, cadena, longitudK)[1]
    return indice


def desviacion(indices):
    suma = 0
    for i in indices:
        suma += i
    promedio = suma/len(indices)
    Desviacion = np.sqrt((i - promedio)**2/(len(indices)))
    return [promedio, Desviacion]


def grafica(longitudCadena, longitudSubcadena, numeroSubcadenas, longitudK):
    ejeY = []
    indices = []
    ejeX = []
    errorY = []

    for i in range(longitudSubcadena - longitudK):
        ejeX.append(longitudK+i)
        for y in range(100):
            ind = indiceDeSimilaridad(
                longitudCadena, longitudSubcadena, numeroSubcadenas, longitudK+i)
            indices.append(ind)
        ejeY.append(desviacion(indices)[0])
        errorY.append(desviacion(indices)[1])

    plt.plot(ejeX, ejeY, "bo", ms=4)
    plt.errorbar(ejeX, ejeY, yerr=errorY, color="red", ecolor="green")
    plt.xlabel("Longitud del kmer")
    plt.ylabel("Indice de similitud")
    plt.title("Variación del indice de similitud respecto a la longitud del kmer")
    plt.show()


# Inicio de Ejecucion

grafica(100, 30, 100, 3)
