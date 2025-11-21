class Solution {
    dijkstra(V, src, adj) {
        const INF = 1e18;
        const dist = Array(V).fill(INF);

        const pq = [];
        const push = (d, u) => {
            pq.push([d, u]);
            let i = pq.length - 1;
            while (i > 0) {
                let p = Math.floor((i - 1) / 2);
                if (pq[p][0] <= pq[i][0]) break;
                [pq[p], pq[i]] = [pq[i], pq[p]];
                i = p;
            }
        };

        const pop = () => {
            const top = pq[0];
            const last = pq.pop();
            if (pq.length > 0) {
                pq[0] = last;
                let i = 0, n = pq.length;
                while (true) {
                    let l = 2 * i + 1, r = 2 * i + 2, smallest = i;
                    if (l < n && pq[l][0] < pq[smallest][0]) smallest = l;
                    if (r < n && pq[r][0] < pq[smallest][0]) smallest = r;
                    if (smallest === i) break;
                    [pq[i], pq[smallest]] = [pq[smallest], pq[i]];
                    i = smallest;
                }
            }
            return top;
        };

        dist[src] = 0;
        push(0, src);

        while (pq.length) {
            const [d, u] = pop();
            if (d !== dist[u]) continue;
            for (const [v, w] of adj[u]) {
                if (dist[v] > d + w) {
                    dist[v] = d + w;
                    push(dist[v], v);
                }
            }
        }
        return dist;
    }

    shortestPath(V, a, b, edges) {
        const INF = 1e18;
        const adj = Array.from({ length: V }, () => []);

        for (const [u, v, w1] of edges) {
            adj[u].push([v, w1]);
            adj[v].push([u, w1]);
        }

        const distA = this.dijkstra(V, a, adj);
        const distB = this.dijkstra(V, b, adj);

        let ans = distA[b];

        for (const [u, v, w1, w2] of edges) {
            if (distA[u] < INF && distB[v] < INF)
                ans = Math.min(ans, distA[u] + w2 + distB[v]);

            if (distA[v] < INF && distB[u] < INF)
                ans = Math.min(ans, distA[v] + w2 + distB[u]);
        }

        return ans >= INF ? -1 : ans;
    }
}