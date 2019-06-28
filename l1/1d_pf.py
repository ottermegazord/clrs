"""
***************************************************************************************
*
*  Name : Idaly Ali
*
*  Description : 1 Dimension Peak Finder
*
***************************************************************************************
"""


def peak_finder(arr):
    """
    Find a peak given an array (assuming there is only 1 peak)
    :param arr: List of numbers
    :return: Peak
    """

    if len(arr) == 0:
        raise TypeError('Empty List')

    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2

    if arr[mid] < arr[mid + 1]:
        return peak_finder(arr[mid:])

    elif arr[mid] < arr[mid-1]:
        return peak_finder(arr[:mid-1])
    else:
        return arr[mid]


arr = [1, 8, 1]

print(peak_finder(arr))