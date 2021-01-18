import sys
arr = sys.argv[1].split(';')
liste = []

x = 0
while x < len(arr):
    liste.append(float(arr[x]))
    x = x + 1


def selection_sort(liste):
   for i in range(len(liste)):
       min = i
       for j in range(i+1, len(liste)):
           if liste[min] > liste[j]:
               min = j
                
       tmp = liste[i]
       liste[i] = liste[min]
       liste[min] = tmp
   return liste

print("Série : ", liste)

selection_sort(liste)

print("Résultat : ", liste)