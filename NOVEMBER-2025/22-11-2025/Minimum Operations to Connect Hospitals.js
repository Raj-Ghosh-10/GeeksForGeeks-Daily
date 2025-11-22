/**
 * @param {number} V
 * @param {number[][]} edges
 * @returns {number}
 */

class Solution {
    minConnect(V, edges) {

        const parent = Array.from({ length: V }, (_, i) => i);
        const rank = Array(V).fill(0);

        const find = (x) => {
            if (parent[x] !== x) parent[x] = find(parent[x]);
            return parent[x];
        };

        const unite = (a, b) => {
            let pa = find(a), pb = find(b);
            if (pa === pb) return;

            if (rank[pa] < rank[pb]) parent[pa] = pb;
            else if (rank[pb] < rank[pa]) parent[pb] = pa;
            else {
                parent[pb] = pa;
                rank[pa]++;
            }
        };

        let redundant = 0;

        for (let [u, v] of edges) {
            if (find(u) === find(v)) redundant++;
            else unite(u, v);
        }

        let components = 0;
        for (let i = 0; i < V; i++) {
            if (find(i) === i) components++;
        }

        let needed = components - 1;
        return redundant >= needed ? needed : -1;
    }
}