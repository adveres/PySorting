"""
A Python module that implements the most common sorting algorithms, tries them on a variety of inputs, and 
outputs some useful reports about what work was done.

This is for fun, and so I can easily remind myself about the algorithms with my own code.
"""
import argparse
import datetime

list1 = [14, 33, 27, 10, 35, 19, 42, 44]
list2 = [0, 56, 73, 12, 5, 99, 19, 65, 27, 30, 2, 66]
list3 = [42, 23, 4, 16, 8, 15]  # Are you lost?
list4 = [1, 2, 100, 3, 4, 101, 6, 5]
list5 = [108, 15, 50, 4, 8, 42, 23, 16]
ALL_SORTABLES = [list1, list2, list3, list4, list5]


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
    https://en.wikipedia.org/wiki/Merge_sort
    Recursively split the array into halves, and then merge the halves back together. This works because you always
    get to a single element eventually, and merging two single-element lists is trivial (you just order them correctly
    and merge into a single list).
    
    O(n * log(n))
    """
    counter = 0
    return _merge_sort(some_list, 0, len(some_list), counter)


def _merge_sort(some_list, l, r, counter):
    counter += 1
    if len(some_list) == 1:  # Base case. Nothing to split.
        return counter, some_list

    # Split the lists down the middle.
    middle = (l+r)/2
    l_list = some_list[l:middle]
    r_list = some_list[middle:r]

    lcount, lsort = _merge_sort(l_list, 0, len(l_list), counter)
    rcount, rsort = _merge_sort(r_list, 0, len(r_list), counter)

    return lcount+rcount, _merge(lsort, rsort)


def _merge(llist, rlist):
    ret_list = []

    while llist or rlist:
        if llist and rlist:  # Both lists non-empty

            # Find which (sorted) sub-list has the smaller val at the front and take it
            if llist[0] <= rlist[0]:
                ret_list.append(llist.pop(0))
            else:
                ret_list.append(rlist.pop(0))

        elif llist:  # Only left list non-empty
            ret_list.extend(llist)
            break
        elif rlist:  # Only right list non-empty
            ret_list.extend(rlist)
            break

        else:        # Both empty. Not possible to hit.
            break

    return ret_list


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
