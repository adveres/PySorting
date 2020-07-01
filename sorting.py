"""
A Python module that implements the most common sorting algorithms, tries them on a variety of inputs, and 
outputs some useful reports about what work was done.

This is for fun, and so I can easily remind myself about the algorithms with my own code.
"""
import argparse
import datetime

from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.selection_sort import selection_sort

list1 = [14, 33, 27, 10, 35, 19, 42, 44]
list2 = [0, 56, 73, 12, 5, 99, 19, 65, 27, 30, 2, 66]
list3 = [42, 23, 4, 16, 8, 15]  # Are you lost?
list4 = [1, 2, 100, 3, 4, 101, 6, 5]
list5 = [108, 15, 50, 4, 8, 42, 23, 16]
list6 = [6, 5, 8, 1, 3, 8, 4, 7, 9, 2]
ALL_SORTABLES = [list1, list2, list3, list4, list5, list6]


def main(algo):
    """
    Main
    """
    for unsorted in ALL_SORTABLES:
        print(unsorted)

        for sorter in sorters:
            if algo is not None and algo != sorter.__name__:
                continue

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
    sorters = [bubble_sort, insertion_sort, merge_sort, selection_sort]

    parser = argparse.ArgumentParser()

    parser.add_argument("--algo", type=str, default=None, choices=[s.__name__ for s in sorters],
                        help='Which sorter to use? If this is not specified, all sorters will be run on all inputs.')

    args = parser.parse_args()

    exit(main(args.algo))
