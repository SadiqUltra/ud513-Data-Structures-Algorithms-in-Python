"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def partition(array):
    length = len(array)
    pivot = length - 1
    low = 0

    while pivot - low > 0:
        if array[low] > array[pivot]:
            if pivot - low > 1:
                array[low], array[pivot-1], array[pivot] = array[pivot - 1], array[pivot], array[low]
                pivot = pivot - 1
            else:
                array[low], array[pivot] = array[pivot], array[low]
                pivot = pivot - 1
                low = low + 1
        else:
            low = low + 1

    return array, pivot


# example = [8, 3, 1, 7, 0, 10, 2]
# print(partition(example))


def quicksort(array):
    if len(array) <= 1:
        return array

    array, pivot = partition(array)

    array[:pivot] = quicksort(array[:pivot])
    array[pivot+1:] = quicksort(array[pivot+1:])

    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
