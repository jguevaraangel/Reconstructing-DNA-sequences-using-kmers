# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:09:17 2019

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

print(permuts(["a","b","c","d"]))
