def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


def quickSort2(array, low, high):
    if low > high:
        return
    base = array[low]
    i = low
    j = high
    while i != j:
        while array[j] >= base and i < j:
            j -= 1
        while array[i] <= base and i < j:
            i += 1
        if i < j:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp

    array[low] = array[i]
    array[i] = base
    quickSort2(array, low, i - 1)
    quickSort2(array, i + 1, high)


print(quickSort([5, 4, 3, 6, 2, 10]))
b = [5, 4, 3, 6, 2, 10]
quickSort2(b, 0, 5)
print(b)
