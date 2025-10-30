class Solution:
    def minOperations(self, arr):
        n=len(arr)
        pq=[-1*item for item in arr]
        heapq.heapify(pq)
        fSum=sum(arr)
        hSum=fSum/2
        ans=0
        while fSum>hSum:
            item=-1*heapq.heappop(pq)
            dec=item/2
            fSum-=dec
            heapq.heappush(pq,-1*dec)
            ans+=1
        return ans