a = [(1, 5)]
b = [(1, 5), (6, 10)]
c = [(1, 5), (1, 5)]
d = [(1, 4), (7, 10), (3, 5)]
e = [
    (-439, 62),
    (-236, 251),
    (-215, -120),
    (-141, 62),
    (-35, 352),
    (59, 163),
    (62, 220),
    (166, 451),
    (199, 391),
    (247, 256),
    (326, 357),
    (360, 414),
    (391, 498),
]
f = [
    (-379, -218),
    (-262, 450),
    (-164, -92),
    (-40, 331),
    (-6, 7),
    (74, 427),
    (236, 270),
    (406, 474),
    (485, 487),
    (497, 498),
]

                                                                                                                                                                                                                                                                                                                                                                                                                      6.30
# ## New theory.
# 1. Check that PN and PN+1(PY) exist
#     - if true, goto 2
#     - if false, end of list, move to 3
# 2. Check Overlap between PX (pair1) and PY
#     - If overlap
#         - generate PN (new pair)
#         - delete both PX and PY
#         - put PN at front of list
#         - recurse, move to step 1. (compare PN which is now @ PX with PY+1, which is now @ PY)
#     - else
#         - (could convert P1 to a diff)
#         - move on to compair P2 and P3
# 3. Completion of 1. means overlaps no longer exist.
#     - sum the remaining differences and return number.
# --Possible problems to keep an eye out for.
#   - negative numbers?
#   - duplicate pairs


def check_overlap(intervals, i, depth, max_depth):
    if i + 1 >= max_depth:
        return
    print(
        f"Current Intervals: {intervals} \nChecking overlap between interval {i}: {intervals[i]} and {i+depth}: {intervals[i + depth]}"
    )
    ## if the final element is larger then either element of the following list item.
    ## Test if the second element can ever be larger?? just included that for logic mapping.

    if (
        intervals[i][1]
        >= intervals[i + depth][0]
        # or intervals[i][1] > intervals[i + depth][1]
    ):
        print("Overlap Found")
        check_overlap(intervals, i, depth + 1, max_depth)
    else:

        new_range = (intervals[i][0], intervals[i + depth - 1][1])
        # print(
        #     f"No overlap found \nNew Range generated: {new_range} \nCurrent Depth:{depth}"
        # )
        ## First remove the elements we are joining.
        ## Should be every one between current i and the depth we reached.
        # print(f"Del elements: {i}:{depth}")
        del intervals[i:depth]
        intervals.append(new_range)
        intervals.sort()
        print(f"Intervals {intervals}")
        ## For some reason intervals does not make it all thew way out
        return


def sum_of_intervals(intervals):
    # Write a function called sumIntervals/sum_intervals() that accepts an array
    # of intervals, and returns the sum of all the interval lengths. Overlapping
    # intervals should only be counted once.

    ## Recursion is slow but fun to think through.
    the_sum = 0
    intervals = list(set(intervals))
    intervals.sort()
    max_depth = len(intervals)
    for index in range(0, max_depth):
        print(f"current index: {index}")
        check_overlap(intervals, index, 1, max_depth)
        max_depth = len(intervals)

    print(intervals)
    for index in range(0, len(intervals)):
        the_sum += intervals[index][1] - intervals[index][0]
    return the_sum


# print(sum_of_intervals(a))
# print(sum_of_intervals(b))
# print(sum_of_intervals(c))
# print(sum_of_intervals(d))
print(sum_of_intervals(f))aaa


# f should be 856
