def quick_sort(array):
    if len(array) < 2:
        return array

    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]

    return quick_sort(menores) + [pivo] + quick_sort(maiores)


print(quick_sort([2, 45, 3, 2, 66, 11, 3, 4, 5, 20, 25, 14, 0, -4, -1]))
