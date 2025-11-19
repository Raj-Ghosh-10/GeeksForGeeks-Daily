class Solution:
    def minCostPath(self, mat):
        hth=len(mat)
        wth=len(mat[0])
        tots=[[float('inf')]*wth for _ in range(hth)]
        import heapq
        hp=[(0,0,0,)]
        tots[0][0]=0
        while hp:
            tot,x,y=heapq.heappop(hp)
            if (x,y)==(wth-1,hth-1):
                return tot
            for dx,dy in [(0,1,),(0,-1,),(1,0,),(-1,0,),]:
                nx,ny=x+dx,y+dy
                if not 0<=nx<wth or not 0<=ny<hth:
                    continue
                cos=abs(mat[ny][nx]-mat[y][x])
                ntot=max(tot,cos)
                if ntot<tots[ny][nx]:
                    tots[ny][nx]=ntot
                    heapq.heappush(hp,(ntot,nx,ny,))