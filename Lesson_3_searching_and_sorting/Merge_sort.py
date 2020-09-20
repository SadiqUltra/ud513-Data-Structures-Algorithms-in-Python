"""Implement merge sort in Python.
Input a list.
Output a sorted list."""


def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1

    merged += left[i:]
    merged += right[j:]

    return merged

# left = [3, 5, 9, 30]
# right = [1, 2, 6, 7]
#
# print(merge(left, right))


def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = int(len(list)/2)
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(merge_sort(test))
