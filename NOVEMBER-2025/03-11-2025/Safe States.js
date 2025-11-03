class Solution {
    safeNodes(V, edges) {
        const revGraph = Array.from({ length: V }, () => []);
        const outdeg = Array(V).fill(0);
        for (let [u, v] of edges) {
            revGraph[v].push(u);
            outdeg[u]++;
        }
        const queue = [];
        const safe = [];
        for (let i = 0; i < V; i++) {
            if (outdeg[i] === 0) queue.push(i);
        }
        while (queue.length) {
            const node = queue.shift();
            safe.push(node);
            for (let parent of revGraph[node]) {
                outdeg[parent]--;
                if (outdeg[parent] === 0) {
                    queue.push(parent);
                }
            }
        }
        safe.sort((a, b) => a - b);
        return safe;
    }
}