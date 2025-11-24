class Solution {
    class DSU {
        int[] parent, size;
        DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }
        int find(int x) {
            if (parent[x] == x) return x;
            return parent[x] = find(parent[x]);
        }
        boolean connected(int a, int b) {
            return find(a) == find(b);
        }
        void unite(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return;
            if (size[a] < size[b]) {
                int t = a; a = b; b = t;
            }
            parent[b] = a;
            size[a] += size[b];
        }
    }
    public int secondMST(int V, int[][] edges) {
        List<int[]> e = new ArrayList<>();
        for (int[] x : edges) e.add(x);
        e.sort((a, b) -> Integer.compare(a[2], b[2]));
        DSU dsu = new DSU(V);
        int mstWeight = 0, mstEdges = 0;
        List<int[]> mstEdgesList = new ArrayList<>();
        for (int[] x : e) {
            int u = x[0], v = x[1], w = x[2];
            if (!dsu.connected(u, v)) {
                dsu.unite(u, v);
                mstWeight += w;
                mstEdges++;
                mstEdgesList.add(new int[]{u, v, w});
            }
        }
        if (mstEdges != V - 1) return -1;
        int secondBest = Integer.MAX_VALUE;
        for (int[] rem : mstEdgesList) {
            int remU = rem[0], remV = rem[1];
            DSU temp = new DSU(V);
            int curWeight = 0, cnt = 0;
            for (int[] x : e) {
                int u = x[0], v = x[1], w = x[2];
                if ((u == remU && v == remV) || (u == remV && v == remU))
                    continue;
                if (!temp.connected(u, v)) {
                    temp.unite(u, v);
                    curWeight += w;
                    cnt++;
                }
            }
            if (cnt == V - 1 && curWeight > mstWeight) {
                secondBest = Math.min(secondBest, curWeight);
            }
        }
        return (secondBest == Integer.MAX_VALUE ? -1 : secondBest);
    }
}