"""Implement bubble sort in Python.
Input a list.
Output a sorted list."""


def bubble_sort(array):
    length = len(array)
    previous = array[0]

    for j in range(length):
        for i in range(1, length):
            if previous > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
            previous = array[i]

    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(bubble_sort(test))
