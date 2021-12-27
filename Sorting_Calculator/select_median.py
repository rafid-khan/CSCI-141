from tools import read_files, sum_calculator
from insertion_sort import swap, insert, insertion_sort, insertion_main
import time
import statistics


def sum_calculator(log):
    """
    This function takes the difference between each location
    and the median location. It utilizes absolute value because
    we are looking for the displacement of each location relative
    to the median. These values are then added to derive the sum.
    """
    optimal_location = statistics.median(log)
    accumulator = 0
    for loc in log:
        accumulator += abs((loc - optimal_location))

    print("Sum of distances to the new store %d" % accumulator)


def quick_select(a_list, k):
    """
    The quicksort function is a more efficient approach to sorting
    compared to the other techniques we have used. By taking in k, as
    a parameter, it is used as a reference point to derive the median
    in this case, in a given list which is also listed as a parameter.
    """
    if len(a_list) > 0:
        pivot = a_list[len(a_list) // 2]
        smaller_list = []
        larger_list = []
        count = 0
        for val in a_list:
            if val < pivot:
                smaller_list.append(int(val))
            if val > pivot:
                larger_list.append(int(val))
            if val == pivot:
                count = +1
        m = len(smaller_list)
        n = m + count
        if m <= k < n:
            return pivot
        elif m > k:
            return quick_select(smaller_list, k)
        else:
            return quick_select(larger_list, k - m - count)


def main():
    """
    This function calls the read_file function
    and this value is then passed through the
    quicksort function. The python time
    module is used to determine the elapsed time
    it takes to sort, and to compute the sum of the
    problem.
    """
    file_name = input("Enter the file name: ")
    lst = []
    with open(file_name) as file_handle:
        for line in file_handle:
            linesplit = line.split()
            lst.append(int(linesplit[1]))
    start_time = time.time()
    quick_select(lst, 3)
    print("Optimum new store location %d" %
          statistics.median(lst))
    sum_calculator(lst)
    print("elapsed time : ", time.time() - start_time)


main()
