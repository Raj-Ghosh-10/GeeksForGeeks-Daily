class Solution {
    int[] parent, rankv;

    int Find(int x) {
        if (parent[x] != x)
            parent[x] = Find(parent[x]);
        return parent[x];
    }

    void Unite(int a, int b) {
        int pa = Find(a), pb = Find(b);
        if (pa == pb) return;

        if (rankv[pa] < rankv[pb]) parent[pa] = pb;
        else if (rankv[pb] < rankv[pa]) parent[pb] = pa;
        else {
            parent[pb] = pa;
            rankv[pa]++;
        }
    }

    public int minConnect(int V, int[,] edges) {
        parent = new int[V];
        rankv = new int[V];

        for (int i = 0; i < V; i++)
            parent[i] = i;

        int E = edges.GetLength(0);
        int redundant = 0;

        for (int i = 0; i < E; i++) {
            int u = edges[i, 0];
            int v = edges[i, 1];

            if (Find(u) == Find(v))
                redundant++;
            else
                Unite(u, v);
        }

        int components = 0;
        for (int i = 0; i < V; i++) {
            if (Find(i) == i)
                components++;
        }

        int need = components - 1;
        return redundant >= need ? need : -1;
    }
}