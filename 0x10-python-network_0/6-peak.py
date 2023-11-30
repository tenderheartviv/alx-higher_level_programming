#!/usr/bin/python3
"""Peak-finding algorithm."""

def find_peak(list_of_integers):
    """Return the peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)

    mid = int(n / 2)
    peak = list_of_integers[mid]
    print(f"Mid: {mid}, Peak: {peak}")

    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        print("Going left")
        return find_peak(list_of_integers[:mid])
    else:
        print("Going right")
        return find_peak(list_of_integers[mid + 1:])

# Test your function
test_list = [1, 3, 20, 4, 1, 0]
result = find_peak(test_list)
print(f"Peak: {result}")

