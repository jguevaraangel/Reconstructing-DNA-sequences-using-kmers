# -*- coding: utf-8 -*-
"""
Created on Sat May  4 23:39:12 2019

@author: juanc
"""

def similarity(cad1,cad2):
    cont = 0
    c = len(cad2)
    for j in range(0, len(cad1)):
        if cad1[j:j+1] == cad2[j:j+1]:
            cont += 1
        elif cad2[j:j+1] == "-":
            c -= 1
    return cont/c

def alignment(cad1,cad2):
    spaces = 0
    dic = {}
    o = ""
    
    for m in range(len(cad1)-len(cad2)):
        spaces += 1
        
    for j in range(spaces + 1):
        comb = cad2 + spaces*"-"
        print(comb)
        s = similarity(cad1,comb)
        dic[s] = comb
        spaces -= 1
        cad2 = "-" + cad2
    comb_list = list(dic.keys())
    maxi = max(comb_list)
    test = dic[maxi]
    for i in test:
        if i != "-":
            o += i
    print(o[0])
#    test = "O"
#    for com in comb_list:
#        if similarity(cad1,com) > similarity(cad1,test):
#            test = com
    return (cad1,o,similarity(cad1,test))

print(alignment("ATACGGCATTA","TCGGGATA"))
print(similarity("ATACGGCATTA","TCGGGATA"))
for i in range(0):
    print("hola")