/**
 * @param {string} s
 * @param {string} t
 * @param {char[][]} transform
 * @param {number[]} cost
 * @returns {number}
 */

class Solution {
    minCost(s, t, transform, cost) {
        const INF = 1e12;
        const dist = Array.from({ length: 26 }, () => Array(26).fill(INF));
        for (let i = 0; i < 26; i++) dist[i][i] = 0;
        for (let i = 0; i < transform.length; i++) {
            const u = transform[i][0].charCodeAt(0) - 97;
            const v = transform[i][1].charCodeAt(0) - 97;
            dist[u][v] = Math.min(dist[u][v], cost[i]);
        }
        for (let k = 0; k < 26; k++) {
            for (let i = 0; i < 26; i++) {
                if (dist[i][k] === INF) continue;
                for (let j = 0; j < 26; j++) {
                    if (dist[k][j] === INF) continue;
                    const newCost = dist[i][k] + dist[k][j];
                    if (newCost < dist[i][j]) dist[i][j] = newCost;
                }
            }
        }
        let total = 0;
        for (let i = 0; i < s.length; i++) {
            let a = s.charCodeAt(i) - 97;
            let b = t.charCodeAt(i) - 97;
            if (a === b) continue;
            let best = INF;
            for (let c = 0; c < 26; c++) {
                if (dist[a][c] < INF && dist[b][c] < INF) {
                    best = Math.min(best, dist[a][c] + dist[b][c]);
                }
            }
            if (best === INF) return -1;
            total += best;
        }
        return total;
    }
}