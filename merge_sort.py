import sys
import time

arr = sys.argv[1].split(';')
liste = []

x = 0
while x < len(arr):
    liste.append(float(arr[x]))
    x = x + 1
    
def mergeSort(liste):
    if len(liste) > 1:
        mid = len(liste)//2
        L = liste[:mid]
        R = liste[mid:]
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                liste[k] = L[i]
                i += 1
            else:
                liste[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            liste[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            liste[k] = R[j]
            j += 1
            k += 1
 
def printList(liste):
    for i in range(len(liste)):
        print(liste[i], end=" ")
    print()


print("Série : ", liste)

start_time = time.time()

mergeSort(liste)

print("Résultat : ", liste)

print("--- %s seconds ---" % (time.time() - start_time))