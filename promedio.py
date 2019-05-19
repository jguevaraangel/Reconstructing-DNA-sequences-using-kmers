# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:32:00 2019


@author: juanc
"""
import secuencia_de_adn
import secuenciador
import ensamblador
import numpy
import matplotlib.pyplot as plt

def indices_sim(loncad,lonsubcad,numsubcad,lonk):
    cad = ""
    bases_nitro = ["A","T","C","G"]
    
    cadena = secuencia_de_adn.cad_adn(loncad,cad,bases_nitro)
    subcadenas = secuenciador.subcads(lonsubcad,numsubcad,cadena)
    kmers = ensamblador.kmer_list(subcadenas,lonsubcad,lonk)
    indice = ensamblador.assembler(kmers,cadena,lonk)[1]
    return indice

def promedio_desviacion(indices):   
    sumaprom = 0
    for i in indices:
        sumaprom += i        
    promedio = sumaprom/len(indices)
    des = numpy.sqrt((i - promedio)**2/(len(indices)))
    return [promedio, des]

def grafica(loncad,lonsubcad,numsubcad,lonk):    
    ejey = []
    indices = []
    ejex = []
    y_errorbar = []
    for i in range(lonsubcad - lonk):
        ejex.append(lonk+i) 
        for y in range(100):
            ind = indices_sim(loncad,lonsubcad,numsubcad,lonk+i)
            indices.append(ind)
        ejey.append(promedio_desviacion(indices)[0])
        y_errorbar.append(promedio_desviacion(indices)[1])
    plt.plot(ejex,ejey,"bo",ms=4)
    plt.errorbar(ejex,ejey,yerr=y_errorbar,color="red",ecolor="green")
    plt.xlabel("Número de kmers")
    plt.ylabel("Indice de similitud")
    plt.title("Variación del indice de similitud respecto al número de kmers")
    plt.show()

#BEG OF EXE
grafica(100,30,100,3)
