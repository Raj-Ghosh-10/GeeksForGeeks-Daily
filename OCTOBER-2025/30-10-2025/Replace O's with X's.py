from collections import deque

class Solution:
    def fill(self, grid):
        n, m = len(grid), len(grid[0])
        q = deque()

        
        for i in range(n):
            if grid[i][0] == 'O':
                q.append((i, 0))
            if grid[i][m - 1] == 'O':
                q.append((i, m - 1))
        for j in range(m):
            if grid[0][j] == 'O':
                q.append((0, j))
            if grid[n - 1][j] == 'O':
                q.append((n - 1, j))

        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y = q.popleft()
            if 0 <= x < n and 0 <= y < m and grid[x][y] == 'O':
                grid[x][y] = '#'  
                for dx, dy in dirs:
                    q.append((x + dx, y + dy))

        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                elif grid[i][j] == '#':
                    grid[i][j] = 'O'