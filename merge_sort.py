import sys
import time

arr = sys.argv[1].split(';')
liste = []

x = 0
while x < len(arr):
    liste.append(float(arr[x]))
    x = x + 1
    

def merge_sort(liste):
    if len(liste) <= 1:
        return liste
    middle = len(liste) // 2
    left_list = liste[:middle]
    right_list = liste[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


print("Série : ", liste)

start_time = time.time()

merge_sort(liste)

print("Résultat : ", liste)

print("--- %s seconds ---" % (time.time() - start_time))