class Solution {
    public int diameter(int V, int[,] edges) {
        List<List<int>> adj = new List<List<int>>();
        for (int i = 0; i < V; i++)
            adj.Add(new List<int>());
        int E = edges.GetLength(0);
        for (int i = 0; i < E; i++) {
            int u = edges[i, 0];
            int v = edges[i, 1];
            adj[u].Add(v);
            adj[v].Add(u);
        }
        var first = BFS(0, adj, V);
        int nodeA = first.Item1;
        var second = BFS(nodeA, adj, V);
        int diameter = second.Item2;
        return diameter;
    }
    private Tuple<int, int> BFS(int start, List<List<int>> adj, int V) {
        int[] dist = new int[V];
        for (int i = 0; i < V; i++) dist[i] = -1;
        Queue<int> q = new Queue<int>();
        q.Enqueue(start);
        dist[start] = 0;
        int farthestNode = start;
        while (q.Count > 0) {
            int node = q.Dequeue();
            foreach (int nei in adj[node]) {
                if (dist[nei] == -1) {
                    dist[nei] = dist[node] + 1;
                    q.Enqueue(nei);
                    if (dist[nei] > dist[farthestNode])
                        farthestNode = nei;
                }
            }
        }
        return new Tuple<int, int>(farthestNode, dist[farthestNode]);
    }
}