class Solution {
    public void fill(char[,] grid) {
        int n = grid.GetLength(0);
        int m = grid.GetLength(1);
        Queue<(int, int)> q = new Queue<(int, int)>();
        for (int i = 0; i < n; i++) {
            if (grid[i, 0] == 'O') q.Enqueue((i, 0));
            if (grid[i, m - 1] == 'O') q.Enqueue((i, m - 1));
        }
        for (int j = 0; j < m; j++) {
            if (grid[0, j] == 'O') q.Enqueue((0, j));
            if (grid[n - 1, j] == 'O') q.Enqueue((n - 1, j));
        }
        int[,] dirs = { {1,0}, {-1,0}, {0,1}, {0,-1} };
        while (q.Count > 0) {
            var (x, y) = q.Dequeue();

            if (x < 0 || y < 0 || x >= n || y >= m || grid[x, y] != 'O')
                continue;

            grid[x, y] = '#';

            for (int k = 0; k < 4; k++) {
                int nx = x + dirs[k, 0];
                int ny = y + dirs[k, 1];
                if (nx >= 0 && ny >= 0 && nx < n && ny < m && grid[nx, ny] == 'O')
                    q.Enqueue((nx, ny));
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i, j] == 'O') grid[i, j] = 'X';
                else if (grid[i, j] == '#') grid[i, j] = 'O';
            }
        }
    }
}