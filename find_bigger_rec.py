def find_bigger_recursion(arr):
    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return arr[0]

    last = arr.pop()
    if arr[-1] <= last:
        arr[-1] = last
        return find_bigger_recursion(arr)
    else:
        return find_bigger_recursion(arr)


print(find_bigger_recursion([]))
