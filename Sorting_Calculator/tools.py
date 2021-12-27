import statistics


def read_files():
    """
    This function opens files, and takes the second
    index from every line, and places it into a new list.
    """
    file_name = input("Enter the file name: ")
    lst = []
    with open(file_name) as file_handle:
        for line in file_handle:
            linesplit = line.split()
            lst.append(int(linesplit[1]))
    return lst


def sum_calculator():
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
