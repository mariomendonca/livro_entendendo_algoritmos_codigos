def sum_recursion(arr):
    if len(arr) == 0:
        return 0

    return arr[0] + sum_recursion(arr[1:len(arr)])


print(sum_recursion([2, 3, 5, 7]))
