# DESCRIPTION
# In this kata, your task is to create all permutations of a non-empty
# input string and remove duplicates, if present.
#
# Create as many "shufflings" as you can!
#
# Examples:
# With input 'a':
# Your function should return: ['a']
#
# With input 'ab':
# Your function should return ['ab', 'ba']
#
# With input 'abc':
# Your function should return ['abc','acb','bac','bca','cab','cba']
#
# With input 'aabb':
# Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

def swap(permutation: list, i: int, j: int) -> list:
    permutation[i], permutation[j] = permutation[j], permutation[i]
    return permutation


def find_i_index(permutation: list) -> int | None:
    for idx in range(len(permutation)-2, -1, -1):
        if permutation[idx] < permutation[idx+1]:
            return idx


def find_j_index(permutation: list, i: int) -> int:
    for idx in range(len(permutation)-1, -1, -1):
        if permutation[idx] > permutation[i]:
            return idx


def reverse_postfix(permutation: list, i: int):
    return permutation[:i+1] + list(reversed(permutation[i+1:]))


def next_permutation(permutation: list) -> list | None:
    i = find_i_index(permutation)
    if i is None:
        return
    j = find_j_index(permutation, i)
    permutation = swap(permutation, i, j)
    return reverse_postfix(permutation, i)


def permutations(s: str) -> list[str]:
    """Generation of permutations based on the Narayana algorithm"""
    permutation = list(s)
    permutation.sort()
    perms = []
    while permutation is not None:
        perms.append(''.join(permutation))
        permutation = next_permutation(permutation)
    return perms


if __name__ == '__main__':
    print(permutations('a'))
    print(permutations('ab'))
    print(permutations('abc'))
    print(permutations('aabb'))
    print(permutations('abcd'))
    print(permutations('123'))
    print(permutations('bwa'))
