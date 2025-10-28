/**
 * @param {number[][]} grid
 * @returns {number[][]}
 */
class Solution {
    nearest(grid) {
        const n = grid.length;
        const m = grid[0].length;
        const dist = Array.from({ length: n }, () => Array(m).fill(-1));
        const queue = [];
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                if (grid[i][j] === 1) {
                    dist[i][j] = 0;
                    queue.push([i, j]);
                }
            }
        }
        const dirs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ];
        let front = 0;
        while (front < queue.length) {
            const [i, j] = queue[front++];
            for (const [dx, dy] of dirs) {
                const ni = i + dx;
                const nj = j + dy;
                if (
                    ni >= 0 && ni < n &&
                    nj >= 0 && nj < m &&
                    dist[ni][nj] === -1
                ) {
                    dist[ni][nj] = dist[i][j] + 1;
                    queue.push([ni, nj]);
                }
            }
        }
        return dist;
    }
}