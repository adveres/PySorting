def insertion_sort(some_list):
    """
    https://en.wikipedia.org/wiki/Insertion_sort
    Split the array into a "sorted" and "unsorted" portion. As we go through the unsorted portion we will backtrack 
    through the sorted portion to INSERT the element-under-inspection into the correct slot.

    O(N^2)
    """
    iters = 0

    # We get to ignore the first element of the unsorted portion, as it becomes the first element of the sorted portion.
    for i in range(1, len(some_list)):
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
