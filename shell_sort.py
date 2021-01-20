import sys
import time

arr = sys.argv[1].split(';')
liste = []

x = 0
while x < len(arr):
    liste.append(float(arr[x]))
    x = x + 1


def shell_sort(liste, n):

    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = liste[i]
            j = i
            while j >= interval and liste[j - interval] > temp:
                liste[j] = liste[j - interval]
                j -= interval

            liste[j] = temp
        interval //= 2

size = len(liste)

print("Série : ", liste)

start_time = time.time()

shell_sort(liste, size)

print("Résultat : ", liste)

print("--- %s seconds ---" % (time.time() - start_time))