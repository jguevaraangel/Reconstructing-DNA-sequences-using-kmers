# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:11:55 2019

@author: juanc
"""

"""Crea subcadenas a partir de la cadena de ADN"""

import random


archivo1 = open("secuenciador_input.txt","r")  #Archivo que tiene la longitud de las subcadenas
#archivo2 = open("numsubcad.txt","r")  #Archivo que tiene el numero de subcadenas
archivo3 = open("subcadenas.txt","w")  #Archivo donde se van a escribir las subcadenas
archivo4 = open("cadena.txt","r")  #Archivo que tiene la cadena de ADN
cadena = archivo4.read()

lonsubcad = int(archivo1.readline().split()[3])
numsubcad = int(archivo1.readline().split()[4])
print(lonsubcad,numsubcad)

subcads = []
for x in range(numsubcad):
    rng = random.Random()
    indice = rng.randrange(0, len(cadena) - (lonsubcad - 1))
    if indice <= len(cadena) - lonsubcad:
        subcadena = ""
        for y in range(lonsubcad):
            subcadena += cadena[indice + y]
        subcads.append(subcadena)

for subcad in subcads:
    archivo3.write(subcad + "\n")
    if not (subcad in cadena):
        print("juemadre!")
    

    
archivo4.close()
archivo3.close()
archivo1.close()


 
