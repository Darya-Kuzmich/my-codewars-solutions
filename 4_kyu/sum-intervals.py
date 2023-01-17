# DESCRIPTION:
# Write a function called sum_of_intervals() that accepts an array
# of intervals, and returns the sum of all the interval lengths.
# Overlapping intervals should only be counted once.

# Intervals
# Intervals are represented by a pair of integers in the form of an array.
# The first value of the interval will always be less than the second value.
# Interval example: [1, 5] is an interval from 1 to 5.
# The length of this interval is 4.

# Overlapping Intervals
# List containing overlapping intervals:
# [
#    [1,4],
#    [7, 10],
#    [3, 5]
# ]
# The sum of the lengths of these intervals is 7.
# Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5],
# which has a length of 4.

def sum_of_intervals(intervals: [list, ...]) -> int:
    intervals.sort()
    total_sum = 0
    for idx in range(len(intervals)):
        if idx > 0:
            if intervals[idx][0] < intervals[idx-1][1] and intervals[idx][1] <= intervals[idx-1][1]:  # noqa
                intervals[idx] = intervals[idx-1]
            elif intervals[idx][0] < intervals[idx-1][1] < intervals[idx][1]:
                total_sum += intervals[idx][1] - intervals[idx-1][1]
            elif intervals[idx][0] >= intervals[idx-1][1]:
                total_sum += intervals[idx][1] - intervals[idx][0]
        else:
            total_sum += intervals[idx][1] - intervals[idx][0]
    return total_sum
