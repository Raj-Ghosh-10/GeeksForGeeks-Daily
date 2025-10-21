from collections import Counter
import heapq
class Solution:
    def topKFreq(self, arr, k):
        freq=Counter(arr)
        return [num for num,_ in heapq.nlargest(k,freq.items(),key=lambda x:(x[1],x[0]))]