class Solution:
    def findPages(self, arr, k):
        lth=len(arr)
        if k>lth:
            return -1
        if k==lth:
            return max(arr)
        
        from itertools import accumulate
        pfs=list(accumulate(arr))
        
        def ok(mid):
            nonlocal k,pfs
            cnt=k
            prv=-1
            prvpfs=0
            for cur in range(lth):
                if pfs[cur]-prvpfs>mid:
                    cnt-=1
                    if cnt<=0:
                        return False
                    prv=cur-1
                    prvpfs=pfs[prv]
            return True
        
        left=max(arr)
        right=pfs[-1]+1
        while left<right:
            mid=left+(right-left)//2
            if not ok(mid):
                left=mid+1
            else:
                right=mid
        return left