# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:11:18 2019

@author: juanc
"""

"""Crea una cadena aleatoria de ADN"""

import random

archivo = open("cadena.txt","w")  #Archivo donde se va a escribir la cadena la cadena de ADN
archivocad = open("loncad.txt","r")  #Archivo que tiene la longitud de la cadena de ADN
u = int(archivocad.read()) 
bases_nitro = ["A","T","C","G"]  #Lista con las bases nitrogenadas de una molecula de ADN
cadena = ""
 
for i in range(u):
    cadena += random.choice(bases_nitro) 
    
archivo.write(cadena)
archivocad.close()
archivo.close()
