class Solution {
    public List<List<int>> nearest(int[,] grid) {
        int n = grid.GetLength(0);
        int m = grid.GetLength(1);
        int[,] dist = new int[n, m];
        bool[,] visited = new bool[n, m];
        Queue<(int, int, int)> q = new Queue<(int, int, int)>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i, j] == 1) {
                    q.Enqueue((i, j, 0));
                    visited[i, j] = true;
                }
            }
        }
        int[] dx = { 1, -1, 0, 0 };
        int[] dy = { 0, 0, 1, -1 };
        while (q.Count > 0) {
            var (i, j, d) = q.Dequeue();
            dist[i, j] = d;
            
            for (int k = 0; k < 4; k++) {
                int ni = i + dx[k];
                int nj = j + dy[k];
                
                if (ni >= 0 && ni < n && nj >= 0 && nj < m && !visited[ni, nj]) {
                    visited[ni, nj] = true;
                    q.Enqueue((ni, nj, d + 1));
                }
            }
        }
        List<List<int>> ans = new List<List<int>>();
        for (int i = 0; i < n; i++) {
            List<int> row = new List<int>();
            for (int j = 0; j < m; j++) {
                row.Add(dist[i, j]);
            }
            ans.Add(row);
        }
        
        return ans;
    }
}