# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:11:55 2019

@author: juanc
"""

"""Crea subcadenas a partir de la cadena de ADN"""

import random

def subcads(lonsubcad,numsubcad,cadena):  #Retorna una lista con subcadenas 
    subcads_list = []
    for x in range(numsubcad):
        rng = random.Random()
        indice = rng.randrange(0, len(cadena) - (lonsubcad - 1))
        subcadena = ""
        for y in range(lonsubcad):
            subcadena += cadena[indice + y]
        subcads_list.append(subcadena)
            
    for subcad in subcads_list:
        archivo2.write(subcad + "\n")
    
#BEG OF EXE
archivo1 = open("secuenciador_input.txt","r")  #Archivo que tiene la longitud de las subcadenas
archivo2 = open("subcadenas.txt","w")  #Archivo donde se van a escribir las subcadenas
archivo3 = open("cadena.txt","r")  #Archivo que tiene la cadena de ADN
cadena = archivo3.read()
lonsubcad = int(archivo1.readline().split()[3])
numsubcad = int(archivo1.readline().split()[4])

subcads(lonsubcad,numsubcad,cadena)

archivo3.close()
archivo2.close()
archivo1.close()


 
