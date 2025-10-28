class Solution:
    def nearest(self, grid):
        n = len(grid)
        m = len(grid[0])
        dist = [[-1 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    dist[i][j] = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            i, j, d = q.popleft()
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] == -1:
                    dist[ni][nj] = d + 1
                    q.append((ni, nj, d + 1))
        return dist