class Solution:
     def searchMatrix(self, mat, x):
        # code here
        from bisect import bisect_left
        
        for r in mat:
            if r[-1] > r[0]:
                i = bisect_left(r, x)
                if i < len(r) and r[i] == x:
                    return True 
            else:
                lo, hi = 0, len(r)-1
                while lo <= hi:
                    mi = lo+(hi-lo)//2
                    if r[mi] == x:
                        return True 
                    am_big = r[mi] >= r[0]
                    x_big = x >= r[0]
                    if am_big == x_big: # on the same side
                        if r[mi] > x:
                            hi = mi-1
                        else:
                            lo = mi+1
                    else:
                        if am_big:
                            lo = mi+1
                        else:
                            hi = mi-1
        return False