def len_rec(arr):
    if len(arr) == 1:
        return 1

    return 1 + len_rec(arr[1:])


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23]

print(len_rec(arr))
print(len(arr))
