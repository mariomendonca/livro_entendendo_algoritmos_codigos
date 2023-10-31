def search_smaller(arr):
    smaller = arr[0]
    smaller_index = 0
    for i in range(len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smaller_index = i

    return smaller_index


def selection_sort(arr):
    new_arr = list()
    for i in range(len(arr)):
        smaller = search_smaller(arr)
        new_arr.append(arr.pop(smaller))
    return new_arr


print(selection_sort([2, 3, 5, 6, 7, 1, 2, 3, 5, 6, 8, 8, 7, 6, 4, 4, 5, 6, 7, 3, 2, 1, 2, 1, 9]))
