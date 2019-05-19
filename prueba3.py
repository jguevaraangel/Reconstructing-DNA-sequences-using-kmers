# -*- coding: utf-8 -*-
"""
Created on Sun May 12 20:41:58 2019

@author: juanc
"""

from itertools import permutations

def permuts(kmers):
    listed_perms = []
    perms = list(permutations(kmers))
    for kmer in perms:
        l_kmer = list(kmer)
        listed_perms.append(l_kmer)
    return listed_perms

hola2 = ["ACTG","TTGA","GGCA"]
print(permuts(hola2))
for i in range(20):
    print(i)