import sys
import time

arr = sys.argv[1].split(';')
liste = []

x = 0
while x < len(arr):
    liste.append(float(arr[x]))
    x = x + 1

def insertion_sort(liste):
    n = 0
    for k in range(1,len(liste)):
        temp=liste[k]
        j=k
        while j>0 and temp<liste[j-1]:
            liste[j]=liste[j-1]
            j-=1
            liste[j]=temp
        n += 1
    print("Nb d'itération :", n)
    return liste

print("Série : ", liste)

start_time = time.time()

insertion_sort(liste)

print("Résultat : ", liste)

print("--- %s seconds ---" % (time.time() - start_time))