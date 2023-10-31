def binary_search(items, item):
    smaller = 0
    bigger = len(items) - 1

    while smaller <= bigger:
        middle = (smaller + bigger) // 2
        attempt = items[middle]

        print(f'smaller: {smaller}, bigger: {bigger}, middle {middle}, attempt: {attempt}')
        if attempt == item:
            return middle
        if attempt > item:
            bigger = middle - 1
        else:
            smaller = middle + 1

    return None


items = [0, 10, 20, 30, 40, 50, 60]

print(binary_search(items, 3))
print(binary_search(items, 50))
