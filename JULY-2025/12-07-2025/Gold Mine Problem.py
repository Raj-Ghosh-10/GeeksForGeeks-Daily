class Solution:
    def maxGold(self, mat):
        hth=len(mat)
        from functools import lru_cache
        @lru_cache(None)
        def dp(y,x=len(mat[0])-1):
            nonlocal mat,hth
            if x==0:
                return mat[y][x]
            mx=0
            for dy in [-1,0,1]:
                ny=y+dy
                if 0<=ny<hth:
                    mx=max(mx,dp(ny,x-1))
            return mx+mat[y][x]
        return max([dp(x) for x in range(hth)])