class Solution:
    def ratInMaze(self, maze):
        # code here
        n=len(maze)
        visited=[[False]*n for i in range(n)]
        res=[]
        def rat(maze,x,y,n,visited,path):
            # Base Condition
            if x==n-1 and y==n-1:
                res.append(path)
                return
            # Boundary Condition
            if x<0 or y<0 or x>=n or y>=n or maze[x][y]==0 or visited[x][y]==True:
                return 
            # choice condition
            visited[x][y]=True
            rat(maze,x-1,y,n,visited,path+"U")
            rat(maze,x+1,y,n,visited,path+"D")
            rat(maze,x,y-1,n,visited,path+"L")
            rat(maze,x,y+1,n,visited,path+"R")
            #Backtracking is visited now started
            visited[x][y]=False
        
        rat(maze,0,0,n,visited,"")
        return sorted(res)