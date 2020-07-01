def selection_sort(some_list):
    """
    https://en.wikipedia.org/wiki/Selection_sort
    Split the list into a sorted/unsorted portion. Go through the list from left to right, starting with position 0 in
    the unsorted portion. When we find the minimum element of the unsorted portion, swap it to the end of the sorted 
    list portion.

    O(N^2)
    """
    iters = 0
    for i in range(0, len(some_list) - 1):
        iters += 1
        min_index = i  # Always reset min for each loop
        for j in range(i + 1, len(some_list)):
            iters += 1
            if some_list[j] < some_list[min_index]:
                min_index = j

        if min_index != i:
            some_list[i], some_list[min_index] = some_list[min_index], some_list[i]

    return iters, some_list
