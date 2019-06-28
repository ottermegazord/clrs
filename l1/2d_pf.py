"""
***************************************************************************************
*
*  Name : Idaly Ali
*
*  Description : 2 Dimension Peak Finder
*
***************************************************************************************
"""

######################
import numpy as np
######################


def peak_finder(arr):
    """
    Find peak given 2D array
    :param arr: 2D array (assuming there is only 1 peak)
    :return: peak
    """
    col = arr.shape[0]

    mid = col // 2
    global_max = max(arr[:, mid])
    # pos = arr.index(global_max)
    pos = int(np.where(arr[:, mid] == global_max)[0])

    if arr[pos][mid-1] > global_max:
        print('first')
        peak_finder(arr[:, mid-1])

    elif arr[pos][mid+1] > global_max:
        print('second')
        peak_finder(arr[:, mid+1])

    else:
        return arr[pos][mid]

arr = np.array([[1, 20, 1, 1], [2, 8, 2, 1], [1, 3, 1, 1]])

print(peak_finder(arr))
