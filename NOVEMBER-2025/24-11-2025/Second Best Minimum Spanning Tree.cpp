class Solution {
public:
    class DSU {
        vector<int> parent, sz;
    public:
        DSU(int n) {
            parent.resize(n + 1);
            sz.resize(n + 1, 1);
            for (int i = 0; i <= n; i++) parent[i] = i;
        }

        int find(int x) {
            return parent[x] == x ? x : parent[x] = find(parent[x]);
        }

        void unite(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return;
            if (sz[a] < sz[b]) swap(a, b);
            parent[b] = a;
            sz[a] += sz[b];
        }

        bool connected(int a, int b) {
            return find(a) == find(b);
        }
    };

    int secondMST(int V, vector<vector<int>> &edges) {
        vector<pair<int,pair<int,int>>> e;
        for (auto &x : edges) e.push_back({x[2], {x[0], x[1]}});
        sort(e.begin(), e.end());

        DSU dsu(V);
        int mstWeight = 0, mstEdges = 0;
        vector<pair<int,int>> mstEdgesList;

        for (auto &x : e) {
            int w = x.first, u = x.second.first, v = x.second.second;
            if (!dsu.connected(u, v)) {
                dsu.unite(u, v);
                mstWeight += w;
                mstEdges++;
                mstEdgesList.push_back({u, v});
            }
        }

        if (mstEdges != V - 1) return -1;

        int secondBest = INT_MAX;

        for (auto &rem : mstEdgesList) {
            DSU temp(V);
            int curWeight = 0, cnt = 0;

            for (auto &x : e) {
                int w = x.first, u = x.second.first, v = x.second.second;
                if (u == rem.first && v == rem.second) continue;
                if (!temp.connected(u, v)) {
                    temp.unite(u, v);
                    curWeight += w;
                    cnt++;
                }
            }

            if (cnt == V - 1 && curWeight > mstWeight)
                secondBest = min(secondBest, curWeight);
        }

        return (secondBest == INT_MAX ? -1 : secondBest);
    }
};