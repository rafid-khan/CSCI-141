"""
Demonstrate sorting a list of unsorted data
using the insertion sort algorithm.
Problem: Insertion Sort
Author: RIT CS Dept.
"""

import random  # to use the shuffle function

from tools import read_files


def swap(lst, i, j):
    """
    swap: List NatNum NatNum -> None
    swap the contents of list at pos i and j.
    Parameters:
        lst - the list of data
        i   - index of one datum
        j   - index of the other datum
    """
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def insert(lst, mark):
    """
    insert: List(Orderable) NatNum -> None
    Move value at index mark+1 so that it is in its proper place.
    The mark is index of the last value in the sorted part.
    Parameters:
        lst - the list of data
        mark - represents cutting the list between
               index mark and index mark+1
    pre-conditions: lst[0:mark+1] is sorted.
    post-conditions: lst[0:mark+2] is sorted.
    """
    index = mark
    while index > -1 and lst[index] > lst[index + 1]:
        swap(lst, index, index + 1)
        index = index - 1


def insertion_sort(lst):
    """
    insertion_sort : List(Orderable) -> None
    Perform an in-place insertion sort on a list of orderable data.
    Parameters:
        lst - the list of data to sort
    post-conditions:
        The data list is in sorted order.
    """
    for mark in range(len(lst) - 1):
        insert(lst, mark)


def insertion_main():
    """
    main : Void -> None
    main creates an unsorted list of Integers of user-given size,
    prints the list, sorts the list and prints the sorted list.
    """

    # create shuffled data
    # N = int(input("Number of elements: "))
    # file_name = input("Enter the file name: ")
    data = []
    # with open(file_name) as file_handle:
    #     for line in file_handle:
    #         data.append(int(line.strip()))
    # for i in range(0, N):
    #   data = data + [i]
    # random.shuffle(data)
    # print("Shuffled data:", data)

    return insertion_sort(data)


# # run program

if __name__ == "__main__":
    insertion_main()
