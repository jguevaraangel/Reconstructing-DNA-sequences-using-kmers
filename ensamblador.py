import random


# Retorna verdadero si la sección final de un kmer es igual a la seccion inicial de otro kmer
def comparaArriba(kmer1, kmer2):
    if kmer1[1:len(kmer1)] == kmer2[0:len(kmer2) - 1]:
        return True


# Retorna verdadero si la sección inicial de un kmer es igual a la seccion final de otro kmer
def comparaAbajo(kmer1, kmer2):
    if kmer1[0:len(kmer1) - 1] == kmer2[1:len(kmer2)]:
        return True


# Retorna un indice que me dice que tan parecidas son dos cadenas
def similarity(cad1, cad2):
    cont = 0
    l = len(cad1)
    for base in range(len(cad1) - len(cad2)):
        cad2 += "-"

    for j in range(0, len(cad1)):
        if cad1[j:j + 1] == cad2[j:j + 1]:
            cont += 1

    return cont/l


# Retorna una lista con todos los kmers no repetidos
def listaKmer(subcadenas, longitudSubcadena, lonK):
    kmers = []
    for subcadena in subcadenas:
        for i in range(longitudSubcadena - lonK + 1):
            kmer = ""
            for x in range(lonK):
                kmer += subcadena[x + i]
            if kmer not in kmers:
                kmers.append(kmer)
    return kmers


# Retorna una cadena y un indice
def alignment(cad1, cad2):
    spaces = 0
    dic = {}
    a_cad = ""
    for m in range(len(cad1)-len(cad2)):
        spaces += 1

    for j in range(spaces+1):
        comb = cad2 + spaces*"-"
        s = similarity(cad1, comb)
        dic[s] = comb
        spaces -= 1
        cad2 = "-" + cad2

    comb_list = list(dic.keys())
    maxi = max(comb_list)
    spacecad = dic[maxi]

    for base in spacecad:
        if base != "-":
            a_cad += base
    return [a_cad, similarity(cad1, spacecad)]


def assembler(kmers, cad, lonk):  # Retorna una cadena o subcadena ensamblada
    assembled_cad = ""

    while len(assembled_cad) != len(cad):
        test = ""
        assembled_cad = ""
        aligned_kmers = []
        leftover_kmers = []
        for kmer in kmers:
            test += kmer[0]
            if kmer == kmers[-1]:
                test += kmer[1:lonk]

        if len(test) != len(cad):
            aligned_kmers.append(kmers[0])
            for i in range(1, len(kmers)):
                if comparaArriba(kmers[i], kmers[0]) == True:
                    aligned_kmers.insert(0, kmers[i])
                elif comparaAbajo(kmers[i], kmers[0]) == True:
                    aligned_kmers.append(kmers[i])
                else:
                    leftover_kmers.append(kmers[i])

            while leftover_kmers != []:
                t = len(leftover_kmers)
                for kmer in leftover_kmers:
                    if comparaArriba(kmer, aligned_kmers[0]) == True:
                        leftover_kmers.remove(kmer)
                        aligned_kmers.insert(0, kmer)
                    elif comparaAbajo(kmer, aligned_kmers[-1]) == True:
                        leftover_kmers.remove(kmer)
                        aligned_kmers.append(kmer)
                if t == len(leftover_kmers):
                    break

            for kmer in aligned_kmers:
                assembled_cad += kmer[0]
                if kmer == aligned_kmers[-1]:
                    assembled_cad += kmer[1:lonk]

            return alignment(cad, assembled_cad)

        aligned_kmers.append(kmers[0])

        for i in range(1, len(kmers)):
            if comparaArriba(kmers[i], kmers[0]) == True:
                aligned_kmers.insert(0, kmers[i])
            elif comparaAbajo(kmers[i], kmers[0]) == True:
                aligned_kmers.append(kmers[i])
            else:
                leftover_kmers.append(kmers[i])

        while leftover_kmers != []:
            i = len(leftover_kmers)
            for kmer in leftover_kmers:
                if comparaArriba(kmer, aligned_kmers[0]) == True:
                    leftover_kmers.remove(kmer)
                    aligned_kmers.insert(0, kmer)
                elif comparaAbajo(kmer, aligned_kmers[-1]) == True:
                    leftover_kmers.remove(kmer)
                    aligned_kmers.append(kmer)
            if i == len(leftover_kmers):
                break

        for kmer in aligned_kmers:
            assembled_cad += kmer[0]
            if kmer == aligned_kmers[-1]:
                assembled_cad += kmer[1:lonk]
        random.shuffle(kmers)
    return [assembled_cad, similarity(cad, assembled_cad)]


# Inicio de Ejecución


# Archivo que tiene las subcadenas generadas por el secuenciador
archivo1 = open("subcadenas.txt", "r")
archivo2 = open("lonK.txt", "r")  # Archivo que tiene la longitud de los kmers
archivo3 = open("cadena.txt", "r")  # Archivo que tiene la cadena de ADN
# Archvio donde se va a escribir la cadena ensamblada
archivo4 = open("cadenaEnsamblada.txt", "w")

subcadenas = archivo1.readlines()
lonk = int(archivo2.readline().split()[5])
cad = archivo3.read()
for i in range(len(subcadenas)):
    subcadenas[i] = subcadenas[i].rstrip("\n")

lonsubcad = len(subcadenas[0])
kmers = listaKmer(subcadenas, lonsubcad, lonk)
assembled_cad = assembler(kmers, cad, lonk)

if len(assembled_cad[0]) != len(cad):
    sim = str(assembled_cad[1])
    archivo4.write("Se ensamblo una sección de la cadena: {0}".format(
        assembled_cad[0]+"\n"))
    archivo4.write("Su indice de similitud es: {0}".format(sim))

else:
    archivo4.write("La cadena ensamblada es: " + assembled_cad[0] + "\n")
    archivo4.write("Su índice de similitud es: " +
                   str(similarity(cad, assembled_cad[0])))

archivo4.close()
archivo3.close()
archivo2.close()
archivo1.close()
