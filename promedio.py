# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:32:00 2019


@author: juanc
"""
import secuencia_de_adn
import secuenciador
import ensamblador
import numpy

def indices_sim(loncad,lonsubcad,numsubcad,lonk):
    cad = ""
    indices = []
    bases_nitro = ["A","T","C","G"]
    
    cadena = secuencia_de_adn.cad_adn(loncad,cad,bases_nitro)
    subcadenas = secuenciador.subcads(lonsubcad,numsubcad,cadena)
    kmers = ensamblador.kmer_list(subcadenas,lonsubcad,lonk)
    indice = ensamblador.assembler(kmers,cadena,lonk)[1]
    indices.append(indice)

def promedio_desviacion(indices):   
    sumaprom = 0
    sumades = 0
    for i in indices:
        sumaprom += i
        sumades += i**2
        
    promedio = sumaprom/len(indices)
    promedio2 = sumades/len(indices)
    des = numpy.sqrt(promedio2 - (promedio)**2)
    return [promedio, des]
    
archivo1 = open("loncad.txt","r")
archivo2 = open("secuenciador_input.txt","r")
archivo3 = open("lonk.txt","r")
#loncad = 50
#lonsubcad = 8
#numsubcad = 100
#lonk = 7
ejey = []
ejey.append(indices_sim(50,8,100,7))
print(ejey)

#for i in range(50):
#    cads = secuencia_de_adn.cad_adn(loncad,cad,bases_nitro)
#    subcadenas = secuenciador.subcads(lonsubcad,numsubcad,cads)
#    kmers = ensamblador.kmer_list(subcadenas,lonsubcad,lonk)
#    indice = ensamblador.assembler(kmers,cads,lonk)[1]
#    indices.append(indice)
# 
#sumaprom = 0
#sumades = 0
#for i in indices:
#    sumaprom += i
#    sumades += i**2
#promedio = sumaprom/len(indices)
#promedio2 = sumades/len(indices)
#des = numpy.sqrt(promedio2 - (promedio)**2)
#print(promedio,"+/-",des)
    
archivo3.close()
archivo2.close()
archivo1.close()