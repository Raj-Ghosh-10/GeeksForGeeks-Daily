class Solution {
    public List<int> safeNodes(int V, int[][] edges) {
        List<int>[] revGraph = new List<int>[V];
        int[] outdeg = new int[V];
        for (int i = 0; i < V; i++)
            revGraph[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            revGraph[v].Add(u);
            outdeg[u]++;
        }
        Queue<int> q = new Queue<int>();
        List<int> safe = new List<int>();
        for (int i = 0; i < V; i++) {
            if (outdeg[i] == 0)
                q.Enqueue(i);
        }
        while (q.Count > 0) {
            int node = q.Dequeue();
            safe.Add(node);
            foreach (int parent in revGraph[node]) {
                outdeg[parent]--;
                if (outdeg[parent] == 0)
                    q.Enqueue(parent);
            }
        }
        safe.Sort();
        return safe;
    }
}