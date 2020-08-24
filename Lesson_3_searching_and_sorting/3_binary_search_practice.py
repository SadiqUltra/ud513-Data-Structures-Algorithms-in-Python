"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
import math

def binary_search(input_array, value):
    """Your code goes here."""
    array_length = len(input_array) - 1
    middle = math.floor(array_length/2)

    while True:
        middle = int(middle)
        middle_value = input_array[middle]

        if (middle == 0 or middle == array_length) and value != middle_value:
            return -1

        if middle_value == value:
            return middle
        elif value < middle_value:
            middle = math.floor(middle / 2) if math.floor(middle / 2) < middle else middle - 1
        elif value > middle_value:
            middle = math.floor((array_length + middle) / 2) if math.floor((array_length + middle) / 2) > middle else middle + 1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
