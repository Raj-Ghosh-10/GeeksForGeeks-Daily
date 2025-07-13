class Solution:
    def nonLisMaxSum(self, arr):
        from bisect import bisect_left
        lth=len(arr)
        lis=[]
        pre=[None]*lth
        tot=0
        for ix,ve in enumerate(arr):
            tot+=ve
            nx=bisect_left(lis,ve,key=lambda ix:arr[ix])
            if nx>=len(lis):
                pre[ix]=lis[-1] if lis else None
                lis.append(ix)
                continue
            pre[ix]=lis[nx-1] if nx-1>=0 else None
            lis[nx]=ix
        sm=0
        cur=lis[-1]
        while cur!=None:
            sm+=arr[cur]
            cur=pre[cur]
        return tot-sm