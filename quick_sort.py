import sys
import time


arr = sys.argv[1].split(';')
liste = []

x = 0
while x < len(arr):
    liste.append(float(arr[x]))
    x = x + 1


def partition(liste, low, high): 
    i = (low-1)
    pivot = liste[high]
  
    for j in range(low, high): 
  
        if liste[j] <= pivot: 
  
            i = i+1
            liste[i], liste[j] = liste[j], liste[i] 
  
    liste[i+1], liste[high] = liste[high], liste[i+1] 
    return (i+1) 
  
  
def quick_sort(liste, low, high): 
    if len(liste) == 1: 
        return liste 
    if low < high: 
  
        pi = partition(liste, low, high) 
  
        quick_sort(liste, low, pi-1) 
        quick_sort(liste, pi+1, high) 

 
n = len(liste) 

print("Série : ", liste)

start_time = time.time()

quick_sort(liste, 0, n-1)

print("Résultat : ", liste)

print("--- %s seconds ---" % (time.time() - start_time))