# DESCRIPTION
# A format for expressing an ordered list of integers is to use a comma
# separated list of either
#
# - individual integers
# - or a range of integers denoted by the starting integer separated from
# the end integer in the range by a dash, '-'. The range includes all integers
# in the interval including both endpoints. It is not considered a range unless
# it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order
# and returns a correctly formatted string in the range format.
#
# Example:
# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])  # noqa
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

def solution(args: list[int]) -> str:
    temp = []
    idx = 0
    span_count = 1
    while idx < len(args) - 1:
        if abs(args[idx] - args[idx+1]) == 1:
            span_count += 1
        else:
            temp.append((idx, span_count))
            span_count = 1
        idx += 1
    temp.append((idx, span_count))
    range_string = ''
    for idx, span_count in temp:
        if span_count == 1:
            range_string += '{},'.format(str(args[idx]))
        elif span_count == 2:
            range_string += '{},{},'.format(str(args[idx-1]), str(args[idx]))
        else:
            range_string += '{}-{},'.format(str(args[idx-span_count+1]), str(args[idx]))  # noqa
    return range_string.rstrip(',')


if __name__ == '__main__':
    print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))  # noqa
    print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))  # noqa
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
