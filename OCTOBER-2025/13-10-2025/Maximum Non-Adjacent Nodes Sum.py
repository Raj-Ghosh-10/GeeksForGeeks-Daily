'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getMaxSum(self, root):
        def solve(node):
            if not node:
                return (0, 0)
            left_include, left_exclude = solve(node.left)
            right_include, right_exclude = solve(node.right)
            include = node.data + left_exclude + right_exclude
            exclude = max(left_include, left_exclude) + max(right_include, right_exclude)
            return (include, exclude)
        include, exclude = solve(root)
        raj = max(include, exclude)
        return raj