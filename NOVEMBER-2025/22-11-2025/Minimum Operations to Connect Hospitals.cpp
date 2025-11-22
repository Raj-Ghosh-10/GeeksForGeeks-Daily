class Solution {
public:
    vector<int> parent, rankv;
    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return;
        
        if (rankv[px] < rankv[py]) {
            parent[px] = py;
        } else if (rankv[px] > rankv[py]) {
            parent[py] = px;
        } else {
            parent[py] = px;
            rankv[px]++;
        }
    }
    int minConnect(int V, vector<vector<int>>& edges) {
        parent.resize(V);
        rankv.resize(V, 0);
        for (int i = 0; i < V; i++)
            parent[i] = i;
        int redundant = 0;
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            if (find(u) == find(v)) {
                redundant++;
            } else {
                unite(u, v);
            }
        }
        int components = 0;
        for (int i = 0; i < V; i++) {
            if (find(i) == i)
                components++;
        }
        int needed = components - 1;
        if (redundant >= needed) return needed;
        return -1;
    }
};