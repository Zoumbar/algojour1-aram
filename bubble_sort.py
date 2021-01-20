import sys
import time

arr = sys.argv[1].split(';')
liste = []

x = 0
while x < len(arr):
    liste.append(float(arr[x]))
    x = x + 1

def bubble_sort(liste):
    n = 0
    for i in range(len(liste)):
        for j in range(len(liste) - 1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
        n += 1
    print("Nb d'itération :", n)

print("Série : ", liste)

start_time = time.time()

bubble_sort(liste)

print("Résultat : ", liste)

print("--- %s seconds ---" % (time.time() - start_time))