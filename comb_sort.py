import sys
import time

arr = sys.argv[1].split(';')
liste = []

x = 0
while x < len(arr):
    liste.append(float(arr[x]))
    x = x + 1


def comb_sort(liste):
    gap = len(liste)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(liste) - gap):
            j = i+gap
            if liste[i] > liste[j]:
                liste[i], liste[j] = liste[j], liste[i]
                swaps = True
 

print("Série : ", liste)

start_time = time.time()

comb_sort(liste)

print("Résultat : ", liste)

print("--- %s seconds ---" % (time.time() - start_time))