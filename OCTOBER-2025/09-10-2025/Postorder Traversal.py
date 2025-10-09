'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        # code here
        if not root:
            return []
        
        stack, result = [root], []
        while stack:
            node = stack.pop()
            result.append(node.data)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return result[::-1]