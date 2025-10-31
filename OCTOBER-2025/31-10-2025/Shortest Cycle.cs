class Solution {
    public int shortCycle(int V, int[,] edges) {
        List<int>[] adj = new List<int>[V];
        for (int i = 0; i < V; i++)
            adj[i] = new List<int>();
        int E = edges.GetLength(0);
        for (int i = 0; i < E; i++) {
            int u = edges[i, 0];
            int v = edges[i, 1];
            adj[u].Add(v);
            adj[v].Add(u);
        }
        int ans = int.MaxValue;
        for (int src = 0; src < V; src++) {
            int[] dist = new int[V];
            int[] parent = new int[V];
            for (int i = 0; i < V; i++) {
                dist[i] = -1;
                parent[i] = -1;
            }
            Queue<int> q = new Queue<int>();
            q.Enqueue(src);
            dist[src] = 0;
            while (q.Count > 0) {
                int node = q.Dequeue();
                foreach (var nbr in adj[node]) {
                    if (dist[nbr] == -1) {
                        dist[nbr] = dist[node] + 1;
                        parent[nbr] = node;
                        q.Enqueue(nbr);
                    }
                    else if (parent[node] != nbr) {
                        ans = Math.Min(ans, dist[node] + dist[nbr] + 1);
                    }
                }
            }
        }
        return (ans == int.MaxValue) ? -1 : ans;
    }
}