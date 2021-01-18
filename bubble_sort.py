def bubble_sort(liste):
    for i in range(len(liste)):
        for j in range(len(liste) - 1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

liste = [1, -2, 3.5, 4]
bubble_sort(liste)
print(liste)