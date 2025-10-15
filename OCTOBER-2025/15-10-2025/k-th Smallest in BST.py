'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def __init__(self):
        self.ans = -1
        self.k = None
        
    def InOrderTraversal(self, root):
        if root == None:
            return
        
        self.InOrderTraversal(root.left)
        self.k -= 1
        if self.k == 0:
            self.ans = root.data
            raise Exception()
            
        self.InOrderTraversal(root.right)
        
    def kthSmallest(self, root, k):
        self.k = k
        try:
            self.InOrderTraversal(root)
        except Exception:
            pass
        return self.ans
        