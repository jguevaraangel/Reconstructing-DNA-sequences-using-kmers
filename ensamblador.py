# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:24:33 2019

@author: juanc
"""

"""Ensambla una cadena y la compara con la cadena de ADN"""
#Nota: Si el programa se queda ejecutando sin fin, es porque hubo un error a la hora de alinear los kmers

def compara(kmer1,kmer2):  #Me retorna verdadero si la sección final de un kmer es igual a la seccion inicial de otro kmer
    if kmer1[1:lonk] == kmer2[0:lonk - 1]:
        return True
        
def compara2(kmer1,kmer2):
    if kmer1[0:lonk - 1] == kmer2[1:lonk]:  #Me retorna verdadero si la sección inicial de un kmer es igual a la seccion final de otro kmer
        return True
    
def similarity(cad, cad_e):  #Me Retorna un indice que me dice que tan parecidas son dos cadenas
    cont = 0
    c = len(cad)
    for j in range(0, len(cad_e)):
        if cad[j:j + 1] == cad_e[j:j + 1]:
            cont += 1
    return cont/c
        
archivo1 = open("subcadenas.txt","r")  #Archivo que tiene las subcadenas generadas por el secuenciador
archivo2 = open("lonsubcad.txt","r")  #Archivo que tiene la longitud de las subcadenas
archivo3 = open("lonk.txt","r")  #Archivo que tiene la longitud de los kmers
archivo4 = open("cadena.txt","r")  #Archivo que tiene la cadena de ADN
archivo5 = open("assembled_cad.txt","w")  #Archvio donde se va a escribir la cadena ensamblada

subcadenas = archivo1.readlines()
lonsubcad = int(archivo2.read())
lonk = int(archivo3.read())
cad = archivo4.read()
listsubcad = []
kmers = []
kmers_norepeated = []
assembled_cad = ""
w = []
y = []

for sub in subcadenas:
    subcad = ""
    for base in sub:
        if base != "\n": 
            subcad += base
    listsubcad.append(subcad)
 
for sub in listsubcad:
    for i in range(lonsubcad - lonk + 1):
        kmer = ""
        for x in range(lonk):
            kmer += sub[x+i]
        kmers.append(kmer)

for kmer in kmers:
    if kmer not in kmers_norepeated:
        kmers_norepeated.append(kmer)

w.append(kmers_norepeated[0])

for i in range(1,len(kmers_norepeated)):
    if compara(kmers_norepeated[i],kmers_norepeated[0]) == True:
        w.insert(0,kmers_norepeated[i])
    elif compara2(kmers_norepeated[i],kmers_norepeated[0]) == True:
        w.append(kmers_norepeated[i])
    else:
        y.append(kmers_norepeated[i])

while y != []:
    for kmer in y:
        if compara(kmer,w[0]) == True:
            y.remove(kmer)
            w.insert(0,kmer)
        elif compara2(kmer,w[-1]) == True:
            y.remove(kmer)
            w.append(kmer)

for kmer in w:
    assembled_cad += kmer[0]
    if kmer == w[-1]:
        assembled_cad += kmer[1:lonk]

archivo5.write(assembled_cad + "\n")
archivo5.write(str(similarity(cad,assembled_cad)))

archivo5.close()
archivo4.close()
archivo3.close()
archivo2.close()
archivo1.close()