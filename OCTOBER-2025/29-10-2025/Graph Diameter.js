/**
 * @param {number} V
 * @param {number[][]} edges
 * @returns {number}
 */
class Solution {
    diameter(V, edges) {
        const adj = Array.from({ length: V }, () => []);
        for (const [u, v] of edges) {
            adj[u].push(v);
            adj[v].push(u);
        }
        const bfs = (start) => {
            const dist = Array(V).fill(-1);
            const queue = [start];
            dist[start] = 0;
            let farthestNode = start;
            while (queue.length) {
                const node = queue.shift();
                for (const nei of adj[node]) {
                    if (dist[nei] === -1) {
                        dist[nei] = dist[node] + 1;
                        queue.push(nei);
                        if (dist[nei] > dist[farthestNode]) {
                            farthestNode = nei;
                        }
                    }
                }
            }
            return [farthestNode, dist[farthestNode]];
        };
        const [nodeA] = bfs(0);
        const [, diameter] = bfs(nodeA);
        return diameter;
    }
}