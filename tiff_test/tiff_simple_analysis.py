from tifffile import imread
import numpy as np
import sys


def get_img_array(filename):

    """
    :param filename: the name of the file or the path to the file if it is not in the same directory
    :type filename: str
    :return: the image data in an array
    """

    return imread(filename)


def get_grid_to_analyze(x_start, x_stop, y_start, y_stop, array):

    """
    This function gets image data for later calculations
    :param x_start: the start position of the desired image data's x axis
    :param x_stop:  the stop position of the desired image data's x axis
    :param y_start: the start position of the desired image data's y axis
    :param y_stop: the stop position of the desired image data's y axis
    :param array: the array to be passed through
    :return: a subset of the original array to be analyzed
    """
    #pre checks on values
    assert x_start >= 0 and x_start < x_stop
    assert x_stop < len(array)
    assert y_start >= 0 and y_start < y_stop
    assert y_stop < len(array[0])

    temp_arr=np.ndarray(shape=(x_stop-x_start,y_stop-y_start))

    #loop that assigns values to the temporary array
    for i in range(x_start,x_stop):
        for j in range(y_start,y_stop):
            temp_arr[i-x_start][j-y_start] = array[i][j]

    return temp_arr


def get_avg_2d(arr):
    """
    This function calculates the average for values in a 2d array
    :param arr: the user selected array
    :return: the average for pixel values
    """
    sum = 0

    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            sum += arr[i][j]

        return sum/arr.size


def get_avg_1d(arr):
    """
    this function calculates the average for a 1d array
    :param arr: the user selected array
    :return: the average for the 1d array
    """
    sum = 0
    for i in range(0,len(arr)):
        sum+=i

    return i/len(arr)


def get_stdev(arr):

    """
    This function calculates the standard deviation for a 2d ndarray
    :param arr: the array to be passed through
    :return: the standard deviation of the array
    """
    #getting mean
    array_avg = get_avg_2d(arr)

    #list and loop to subtract mean from each val
    mean_subtracted = []
    for i in range(0,len(arr)):
        for j in range(0, len(arr[0])):
            mean_subtracted.append((arr[i][j] - array_avg)**2)

    #finding mean of subtracted list
    sub_mean = get_avg_1d(mean_subtracted)

    #returning sqrt of the subtracted and squared mean to get stdev
    return np.sqrt(sub_mean)

def get_min(arr):

    """
    this function gets the minimum value in the array
    :param arr: the array to be passed through
    :return: the minimum value
    """

    min_val = sys.maxsize

    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if arr[i][j] < min_val:
                min_val = arr[i][j]

    return min_val

def get_max(arr):
    """
        this function gets the max value in the array
        :param arr: the array to be passed through
        :return: the maximum value
        """

    max_val = -sys.maxsize

    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if arr[i][j] > max_val:
                max_val = arr[i][j]

    return max_val


array = get_grid_to_analyze(0,2047,0,2047,get_img_array("Ni300K.tif"))

print("Standard deviataion for Pixels: " + str(get_stdev(array)))
print("pixel value average: " + str(get_avg_2d(array)))
print("pixel value minimum:" + str(get_min(array)))
print("pixel value maximum: " + str(get_max(array)))
print("total pixels observed: " + str(array.size))
