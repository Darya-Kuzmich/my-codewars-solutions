# DESCRIPTION:
# You are given a binary tree:
#
# class Node:
#     def __init__(self, L, R, n):
#         self.left = L
#         self.right = R
#         self.value = n
#
# Your task is to return the list with elements from tree sorted by levels,
# which means the root element goes first, then root children
# (from left to right) are second and third, and so on.
#
# Return empty list if root is None.
#
# Example 1 - following tree:
#
#                  2
#             8        9
#           1  3     4   5
# Should return following list:
#
# [2,8,9,1,3,4,5]
# Example 2 - following tree:
#
#                  1
#             8        4
#               3        5
#                          7
# Should return following list:
#
# [1,8,4,3,5,7]

from collections import deque


class Node:

    def __init__(self, L, R, n: int):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node: Node) -> list:
    values = []
    nodes_queue = deque()
    visited = []
    nodes_queue.append(node)
    while nodes_queue:
        node = nodes_queue.popleft()
        if node and node not in visited:
            values.append(node.value)
            visited.append(node)
            nodes_queue.append(node.left)
            nodes_queue.append(node.right)
    return values
