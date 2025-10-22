import heapq
class Solution:
    def nearlySorted(self, arr, k):  
        pq=[]
        l=0
        for r in range(len(arr)):
            heapq.heappush(pq,arr[r])
            if len(pq)>k:
                arr[l]=heapq.heappop(pq)
                l+=1
        while pq:
            arr[l]=heapq.heappop(pq)
            l+=1