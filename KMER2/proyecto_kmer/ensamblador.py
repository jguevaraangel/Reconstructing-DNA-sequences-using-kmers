# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:24:33 2019

@author: juanc
"""

"""Ensambla una cadena y la compara con la cadena de ADN"""

import random

def compara_arriba(kmer1,kmer2):  #Retorna verdadero si la sección final de un kmer es igual a la seccion inicial de otro kmer
    if kmer1[1:lonk] == kmer2[0:lonk - 1]:
        return True
        
def compara_abajo(kmer1,kmer2):
    if kmer1[0:lonk - 1] == kmer2[1:lonk]:  #Retorna verdadero si la sección inicial de un kmer es igual a la seccion final de otro kmer
        return True
    
def similarity(cad, cad_e):  #Retorna un indice que me dice que tan parecidas son dos cadenas
    cont = 0
    c = len(cad)
    for base in range(len(cad) - len(cad_e)):
        cad_e += "-"
        
    for j in range(0, len(cad)):
        if cad[j:j + 1] == cad_e[j:j + 1]:
            cont += 1
        elif cad_e[j:j+1] == "-":
            c -= 1
            
    return cont/c

def kmer_list(subcadenas,lonsubcad,lonk): #Retorna una lista con todos los kmers no repetidos
    kmers = []
    for sub in subcadenas:
        for i in range(lonsubcad - lonk + 1):
            kmer = ""
            for x in range(lonk):
                kmer += sub[x + i]
            if kmer not in kmers:   
                kmers.append(kmer)
    return kmers

def alignment(cad1,cad2):
    spaces = 0
    dic = {}
    a_cad = ""
    for m in range(len(cad1)-len(cad2)):
        spaces += 1
        
    for j in range(spaces + 1):
        comb = cad2 + spaces*"-"
        s = similarity(cad1,comb)
        dic[s] = comb
        spaces -= 1
        cad2 = "-" + cad2
        
    comb_list = list(dic.keys())
    maxi = max(comb_list)
    spacecad = dic[maxi]
    
    for base in spacecad:
        if base != "-":
            a_cad += base
    
    index = cad1.find(a_cad,0)
    
    return [a_cad, index, len(cad2), similarity(cad1,spacecad)]

def assembler(kmers,aligned_kmers,leftover_kmers,cad,lonk):  #Retorna una cadena ensamblada
    test = ""
    assembled_cad = ""
    while len(assembled_cad) != len(cad):
        for kmer in kmers:
            test += kmer[0]
            if kmer == kmers[-1]:
                test += kmer[1:lonk]
                
        if len(test) != len(cad):
            aligned_kmers.append(kmers[0])
            for i in range(1,len(kmers)):
                if compara_arriba(kmers[i],kmers[0]) == True:
                    aligned_kmers.insert(0,kmers[i])
                elif compara_abajo(kmers[i],kmers[0]) == True:
                    aligned_kmers.append(kmers[i])
                else:
                     leftover_kmers.append(kmers[i])
                     
            while leftover_kmers != []:
                i = len(leftover_kmers)
                for kmer in leftover_kmers:
                    if compara_arriba(kmer, aligned_kmers[0]) == True:
                        leftover_kmers.remove(kmer)
                        aligned_kmers.insert(0,kmer)
                    elif compara_abajo(kmer, aligned_kmers[-1]) == True:
                        leftover_kmers.remove(kmer)
                        aligned_kmers.append(kmer)
                if i == len(leftover_kmers):
                    break
    
            for kmer in aligned_kmers:
                assembled_cad += kmer[0]
                if kmer == aligned_kmers[-1]:
                    assembled_cad += kmer[1:lonk]
            print(len(test))
            print(len(assembled_cad))
            print(alignment(cad,assembled_cad))
            return alignment(cad,assembled_cad)
        
        aligned_kmers.append(kmers[0])
        
        for i in range(1,len(kmers)):
                if compara_arriba(kmers[i],kmers[0]) == True:
                    aligned_kmers.insert(0,kmers[i])
                elif compara_abajo(kmers[i],kmers[0]) == True:
                    aligned_kmers.append(kmers[i])
                else:
                    leftover_kmers.append(kmers[i])

        while leftover_kmers != []:
                i = len(leftover_kmers)
                for kmer in leftover_kmers:
                    if compara_arriba(kmer, aligned_kmers[0]) == True:
                        leftover_kmers.remove(kmer)
                        aligned_kmers.insert(0,kmer)
                    elif compara_abajo(kmer, aligned_kmers[-1]) == True:
                        leftover_kmers.remove(kmer)
                        aligned_kmers.append(kmer)
                if i == len(leftover_kmers):
                    break
    
        for kmer in aligned_kmers:
                assembled_cad += kmer[0]
                if kmer == aligned_kmers[-1]:
                    assembled_cad += kmer[1:lonk]
        
        random.shuffle(kmers)
    
    print(test)
    print(len(test))
    print(assembled_cad)
    return assembled_cad
    
#BEG OF EXE
archivo1 = open("subcadenas.txt","r")  #Archivo que tiene las subcadenas generadas por el secuenciador
archivo2 = open("lonk.txt","r")  #Archivo que tiene la longitud de los kmers
archivo3 = open("cadena.txt","r")  #Archivo que tiene la cadena de ADN
archivo4 = open("assembled_cad.txt","w")  #Archvio donde se va a escribir la cadena ensamblada

subcadenas = archivo1.readlines()
lonk = int(archivo2.readline().split()[5])
cad = archivo3.read()
aligned_kmers = []
leftover_kmers = []

for i in range(len(subcadenas)):
    subcadenas[i] = subcadenas[i].rstrip("\n") 

lonsubcad = len(subcadenas[0])
kmers = kmer_list(subcadenas,lonsubcad,lonk)
assembled_cad = assembler(kmers, aligned_kmers, leftover_kmers,cad,lonk)
print(len(cad))
print(assembled_cad)

if type(assembled_cad) == list:
    ini = str(assembled_cad[1])
    fin = str(assembled_cad[2])
    sim = str(assembled_cad[3])
    archivo4.write("Se ensamblo una sección de la cadena: {0}".format(assembled_cad[0]+"\n"))
    archivo4.write("La cadena ensamblada se encuentra en: [{0}:{1}]".format(ini,fin)+"\n")
    archivo4.write("Su indice de similitud es: {0}".format(sim))
    
else:
    archivo4.write("La cadena ensamblada es: " + assembled_cad + "\n")
    archivo4.write("Su índice de similitud es: " + str(similarity(cad,assembled_cad)))

archivo4.close()
archivo3.close()
archivo2.close()
archivo1.close()
