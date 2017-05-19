"""
A Python module that implements the most common sorting algorithms, tries them on a variety of inputs, and 
outputs some useful reports about what work was done.

This is for fun, and so I can easily remind myself about the algorithms with my own code.
"""
import datetime

list1 = [14, 33, 27, 10, 35, 19, 42, 44]
list2 = [0, 56, 73, 12, 5, 99, 19, 65, 27, 30, 2, 66]
list3 = [42, 23, 4, 16, 8, 15]  # Are you lost?
ALL_SORTABLES = [list1, list2, list3]


def bubble_sort(some_list):
    """
    https://en.wikipedia.org/wiki/Bubble_sort
    We continuously loop through the data set, swapping next-door-neighbors that are out of order. In this way,
    values will BUBBLE one spot towards their correct positions once per loop.

    O(N^2)
    """
    iters = 0
    did_swap = True

    while did_swap:
        did_swap = False  # Turn off sentinal
        iters += 1

        for i in xrange(0, len(some_list) - 1):
            iters += 1
            if some_list[i] > some_list[i + 1]:
                some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
                did_swap = True  # Activate sentinal, we had to do work.

    return iters, some_list


def insertion_sort(some_list):
    """
    https://en.wikipedia.org/wiki/Insertion_sort
    Split the array into a "sorted" and "unsorted" portion. As we go through the unsorted portion we will backtrack 
    through the sorted portion to INSERT the element-under-inspection into the correct slot.

    O(N^2)
    """
    iters = 0

    # We get to ignore the first element of the unsorted portion, as it becomes the first element of the sorted portion.
    for i in xrange(1, len(some_list)):
        iters += 1

        # Keep track of where we are in the unsorted portion of the list.
        elem = some_list[i]
        hole_pos = i  # hole_pos is index, in unsorted portion, of the hole

        # We're iterating right to left. We want to stop iterating when the element to the left of our hole position is
        # less than the element we're trying to insert.
        while (hole_pos > 0) and (some_list[hole_pos - 1] > elem):
            iters += 1
            # Shift each element one space to the right. Keeps a clear space for our insertion.
            some_list[hole_pos] = some_list[hole_pos - 1]
            # Continue to move left.
            hole_pos = hole_pos - 1

        # Insert the element into the sorted portion of the list where the hole is.
        some_list[hole_pos] = elem

    return iters, some_list


def merge_sort(some_list):
    """
    TODO 
    """
    pass


def selection_sort(some_list):
    """
    https://en.wikipedia.org/wiki/Selection_sort
    Split the list into a sorted/unsorted portion. Go through the list from left to right, starting with position 0 in
    the unsorted portion. When we find the minimum element of the unsorted portion, swap it to the end of the sorted 
    list portion.

    O(N^2)
    """
    iters = 0
    for i in xrange(0, len(some_list) - 1):
        iters += 1
        min_index = i  # Always reset min for each loop
        for j in xrange(i + 1, len(some_list)):
            iters += 1
            if some_list[j] < some_list[min_index]:
                min_index = j

        if min_index != i:
            some_list[i], some_list[min_index] = some_list[min_index], some_list[i]

    return iters, some_list


def main():
    """
    Main
    """
    sorters = [bubble_sort, insertion_sort, selection_sort]

    for unsorted in ALL_SORTABLES:
        print(unsorted)

        for sorter in sorters:
            # Sort the thing, and time it.
            start = datetime.datetime.now()
            iters, sorted_list = sorter(list(unsorted))
            time_delta = datetime.datetime.now() - start

            # Make sure it even worked.
            if sorted_list != sorted(unsorted):
                print("    FAILURE!!! {} did not successfully sort {}.".format(sorter.__name__, unsorted))
                print("        Got: {}".format(sorted_list))
            else:
                print("    {0: <14} sorted in {1: <3} iterations and took: {2}".format(sorter.__name__,
                                                                                       iters,
                                                                                       time_delta))

        print("")


if __name__ == "__main__":
    exit(main())
