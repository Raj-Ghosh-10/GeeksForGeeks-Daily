/**
 * @param {number} V
 * @param {number[][]} edges
 * @returns {number}
 */

class Solution {
    shortCycle(V, edges) {
        const adj = Array.from({ length: V }, () => []);
        for (let [u, v] of edges) {
            adj[u].push(v);
            adj[v].push(u);
        }
        let ans = Infinity;
        for (let src = 0; src < V; src++) {
            const dist = Array(V).fill(-1);
            const parent = Array(V).fill(-1);
            const queue = [];
            queue.push(src);
            dist[src] = 0;
            while (queue.length > 0) {
                let node = queue.shift();
                for (let nbr of adj[node]) {
                    if (dist[nbr] === -1) {
                        dist[nbr] = dist[node] + 1;
                        parent[nbr] = node;
                        queue.push(nbr);
                    }
                    else if (parent[node] !== nbr) {
                        ans = Math.min(ans, dist[node] + dist[nbr] + 1);
                    }
                }
            }
        }
        return ans === Infinity ? -1 : ans;
    }
}