class Solution {
    class DSU {
        int[] parent, size;

        public DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }

        public bool Connected(int a, int b) {
            return Find(a) == Find(b);
        }

        public void Unite(int a, int b) {
            a = Find(a);
            b = Find(b);
            if (a == b) return;
            if (size[a] < size[b]) {
                int t = a; a = b; b = t;
            }
            parent[b] = a;
            size[a] += size[b];
        }
    }

    public int secondMST(int V, int[,] edges) {
        int E = edges.GetLength(0);
        var list = new List<(int w, int u, int v)>();
        for (int i = 0; i < E; i++)
            list.Add((edges[i,2], edges[i,0], edges[i,1]));

        list.Sort((a, b) => a.w.CompareTo(b.w));

        var dsu = new DSU(V);
        int mst = 0, cnt = 0;
        var mstList = new List<(int u, int v, int w)>();

        foreach (var x in list) {
            if (!dsu.Connected(x.u, x.v)) {
                dsu.Unite(x.u, x.v);
                mst += x.w;
                cnt++;
                mstList.Add((x.u, x.v, x.w));
            }
        }

        if (cnt != V - 1) return -1;

        int ans = int.MaxValue;

        foreach (var rem in mstList) {
            var t = new DSU(V);
            int cur = 0, used = 0;

            foreach (var x in list) {
                if ((x.u == rem.u && x.v == rem.v) || (x.u == rem.v && x.v == rem.u))
                    continue;

                if (!t.Connected(x.u, x.v)) {
                    t.Unite(x.u, x.v);
                    cur += x.w;
                    used++;
                }
            }

            if (used == V - 1 && cur > mst)
                ans = Math.Min(ans, cur);
        }

        return ans == int.MaxValue ? -1 : ans;
    }
}