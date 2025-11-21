class Solution {
    static final long INF = (long)1e18;

    long[] dijkstra(int V, int src, ArrayList<ArrayList<int[]>> adj) {
        long[] dist = new long[V];
        Arrays.fill(dist, INF);

        PriorityQueue<long[]> pq = new PriorityQueue<>((x, y) -> Long.compare(x[0], y[0]));
        dist[src] = 0;
        pq.add(new long[]{0, src});

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int u = (int)cur[1];

            if (d != dist[u]) continue;

            for (int[] nxt : adj.get(u)) {
                int v = nxt[0], w = nxt[1];
                if (dist[v] > d + w) {
                    dist[v] = d + w;
                    pq.add(new long[]{dist[v], v});
                }
            }
        }
        return dist;
    }

    public int shortestPath(int V, int a, int b, int[][] edges) {

        ArrayList<ArrayList<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());

        for (int[] e : edges) {
            int u = e[0], v = e[1], w1 = e[2];
            adj.get(u).add(new int[]{v, w1});
            adj.get(v).add(new int[]{u, w1});
        }

        long[] distA = dijkstra(V, a, adj);
        long[] distB = dijkstra(V, b, adj);

        long ans = distA[b];

        for (int[] e : edges) {
            int u = e[0], v = e[1], w2 = e[3];

            if (distA[u] < INF && distB[v] < INF)
                ans = Math.min(ans, distA[u] + w2 + distB[v]);

            if (distA[v] < INF && distB[u] < INF)
                ans = Math.min(ans, distA[v] + w2 + distB[u]);
        }

        return ans >= INF ? -1 : (int)ans;
    }
}