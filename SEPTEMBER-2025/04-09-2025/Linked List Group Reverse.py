"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def swap_in_pairs(self,arr, k):
        n = len(arr)
        for i in range(0, n, k):
            arr[i:i+k] = reversed(arr[i:i+k])
        return arr

    def reverseKGroup(self, head, k):
        initans=[]
        new=head
        while new:
            initans.append(new.data)
            new=new.next
        overAllAns=self.swap_in_pairs(initans,k)
        current=head
        cons=0
        while current:
            current.data=overAllAns[cons]
            cons+=1
            current=current.next
        return head