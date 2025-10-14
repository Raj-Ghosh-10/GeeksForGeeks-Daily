"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def nodeSum(self, root, l, r):
        if not root:
            return 0
        
        raj = 0
        if l <= root.data <= r:
            raj += root.data
        if root.data > l:
            raj += self.nodeSum(root.left, l, r)
        if root.data < r:
            raj += self.nodeSum(root.right, l, r)
        return raj