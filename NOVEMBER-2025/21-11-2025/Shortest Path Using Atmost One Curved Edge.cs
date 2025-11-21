using System;
using System.Collections.Generic;

public class Solution {

    const long INF = (long)1e18;

    class Node : IComparable<Node> {
        public long dist;
        public int u;
        public Node(long d, int x) { dist = d; u = x; }
        public int CompareTo(Node other) {
            return dist.CompareTo(other.dist);
        }
    }

    long[] Dijkstra(int V, int src, List<int[]>[] adj) {

        long[] dist = new long[V];
        for (int i = 0; i < V; i++) dist[i] = INF;

        var pq = new SortedSet<Node>(Comparer<Node>.Create((a,b) =>
            a.dist == b.dist ? a.u.CompareTo(b.u) : a.dist.CompareTo(b.dist)
        ));

        dist[src] = 0;
        pq.Add(new Node(0, src));

        while (pq.Count > 0) {
            Node top = pq.Min;
            pq.Remove(top);

            long d = top.dist;
            int u = top.u;

            if (d != dist[u]) continue;

            foreach (var edge in adj[u]) {
                int v = edge[0];
                int w = edge[1];

                if (dist[v] > d + w) {
                    dist[v] = d + w;
                    pq.Add(new Node(dist[v], v));
                }
            }
        }

        return dist;
    }

    public int shortestPath(int V, int a, int b, int[,] edges) {

        List<int[]>[] adj = new List<int[]>[V];
        for (int i = 0; i < V; i++)
            adj[i] = new List<int[]>();

        int E = edges.GetLength(0);

        for (int i = 0; i < E; i++) {
            int u = edges[i, 0];
            int v = edges[i, 1];
            int w1 = edges[i, 2];

            adj[u].Add(new int[] { v, w1 });
            adj[v].Add(new int[] { u, w1 });
        }

        long[] distA = Dijkstra(V, a, adj);
        long[] distB = Dijkstra(V, b, adj);

        long ans = distA[b];

        for (int i = 0; i < E; i++) {
            int u = edges[i, 0];
            int v = edges[i, 1];
            int w2 = edges[i, 3];

            if (distA[u] < INF && distB[v] < INF)
                ans = Math.Min(ans, distA[u] + w2 + distB[v]);

            if (distA[v] < INF && distB[u] < INF)
                ans = Math.Min(ans, distA[v] + w2 + distB[u]);
        }

        return ans >= INF ? -1 : (int)ans;
    }
}