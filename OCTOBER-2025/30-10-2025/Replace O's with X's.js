/**
 * @param {character[][]} grid
 * @returns {void}
 */
class Solution {
    fill(grid) {
        const n = grid.length;
        const m = grid[0].length;
        const queue = [];
        for (let i = 0; i < n; i++) {
            if (grid[i][0] === 'O') queue.push([i, 0]);
            if (grid[i][m - 1] === 'O') queue.push([i, m - 1]);
        }
        for (let j = 0; j < m; j++) {
            if (grid[0][j] === 'O') queue.push([0, j]);
            if (grid[n - 1][j] === 'O') queue.push([n - 1, j]);
        }
        const dirs = [[1,0], [-1,0], [0,1], [0,-1]];
        while (queue.length) {
            const [x, y] = queue.shift();
            if (x < 0 || y < 0 || x >= n || y >= m || grid[x][y] !== 'O') continue;
            grid[x][y] = '#';
            for (const [dx, dy] of dirs) {
                const nx = x + dx, ny = y + dy;
                if (nx >= 0 && ny >= 0 && nx < n && ny < m && grid[nx][ny] === 'O') {
                    queue.push([nx, ny]);
                }
            }
        }
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                if (grid[i][j] === 'O') grid[i][j] = 'X';
                else if (grid[i][j] === '#') grid[i][j] = 'O';
            }
        }
    }
}