class Solution {
    int[] parent, rank;

    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int a, int b) {
        int pa = find(a), pb = find(b);
        if (pa == pb) return;
        if (rank[pa] < rank[pb]) parent[pa] = pb;
        else if (rank[pb] < rank[pa]) parent[pb] = pa;
        else {
            parent[pb] = pa;
            rank[pa]++;
        }
    }
    public int minConnect(int V, int[][] edges) {
        parent = new int[V];
        rank = new int[V];
        for (int i = 0; i < V; i++) parent[i] = i;
        int redundant = 0;
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            if (find(u) == find(v)) redundant++;
            else unite(u, v);
        }
        int components = 0;
        for (int i = 0; i < V; i++) {
            if (find(i) == i) components++;
        }
        int need = components - 1;
        if (redundant >= need) return need;
        return -1;
    }
}