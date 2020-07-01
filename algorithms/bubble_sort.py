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

        for i in range(0, len(some_list) - 1):
            iters += 1
            if some_list[i] > some_list[i + 1]:
                some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
                did_swap = True  # Activate sentinal, we had to do work.

    return iters, some_list
