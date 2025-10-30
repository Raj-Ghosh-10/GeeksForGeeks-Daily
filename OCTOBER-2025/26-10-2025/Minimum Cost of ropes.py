class Solution:
    def minCost(self, arr):
        heapq.heapify(arr)
        ans=0
        while len(arr)!=1:
            cost=heapq.heappop(arr)+heapq.heappop(arr)
            ans+=cost
            heapq.heappush(arr,cost)
        return ans