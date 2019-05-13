# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:11:18 2019

@author: juanc
"""

"""Crea una cadena aleatoria de ADN"""

import random

def cad_adn(loncad,cadena,bases_nitro):  #Retorna una cadena de ADN aleatoria
    for i in range(loncad):
        cadena += random.choice(bases_nitro)
    return cadena

#BEG OF EXE
archivo1 = open("cadena.txt","w")  #Archivo donde se va a escribir la cadena la cadena de ADN
archivo2 = open("loncad.txt","r")  #Archivo que tiene la longitud de la cadena de ADN
loncad = int(archivo2.readline().split()[5]) 
bases_nitro = ["A","T","C","G"]  #Lista con las bases nitrogenadas de una molecula de ADN
cadena = ""

archivo1.write(cad_adn(loncad,cadena,bases_nitro))
archivo2.close()
archivo1.close()
