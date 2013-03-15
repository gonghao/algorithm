#!/usr/bin/env python

def insertionSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] < key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key

if __name__ == '__main__':
    arrayText = raw_input('Input all numbers need to sort with SPACE seperated:\n')
    array = arrayText.split(' ')
    array = map(int, array)
    insertionSort(array)
    print array
