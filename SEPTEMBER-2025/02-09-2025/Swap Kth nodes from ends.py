'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        # code here
        first=head
        s1=None
        s2=head
        for i in range(k):
            if i==k-1:
                s1=first
            if not first:
                return head
            first=first.next
        while first:
            s2=s2.next
            first=first.next
        s1.data, s2.data=s2.data, s1.data
        return head