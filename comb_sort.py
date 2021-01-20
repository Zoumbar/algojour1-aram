import sys
import time


arr = sys.argv[1].split(';')
liste = []

x = 0
while x < len(arr):
    liste.append(float(arr[x]))
    x = x + 1

def comb_sort(liste):
    n = 0
    total = len(liste)
    change = True
    while total > 1 or change:
        total = max(1, int(total / 1.25))
        change = False
        for a in range(len(liste) - total):
            b = a+total
            if liste[a] > liste[b]:
                liste[a], liste[b] = liste[b], liste[a]
                change = True
        n += 1
    print("Nb d'itération :", n)

print("Série : ", liste)

start_time = time.time()

comb_sort(liste)

print("Résultat : ", liste)

print("--- %s seconds ---" % (time.time() - start_time))