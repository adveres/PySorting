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
    middle = int((l + r) / 2)
    l_list = some_list[l:middle]
    r_list = some_list[middle:r]

    lcount, lsort = _merge_sort(l_list, 0, len(l_list), counter)
    rcount, rsort = _merge_sort(r_list, 0, len(r_list), counter)

    return lcount + rcount, _merge(lsort, rsort)


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

        else:  # Both empty. Not possible to hit.
            break

    return ret_list
