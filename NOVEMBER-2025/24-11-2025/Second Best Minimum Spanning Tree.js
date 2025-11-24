class Solution {
    secondMST(V, edges) {
        class DSU {
            constructor(n) {
                this.p = Array.from({ length: n }, (_, i) => i);
                this.sz = Array(n).fill(1);
            }
            find(x) {
                return this.p[x] === x ? x : (this.p[x] = this.find(this.p[x]));
            }
            connected(a, b) {
                return this.find(a) === this.find(b);
            }
            unite(a, b) {
                a = this.find(a);
                b = this.find(b);
                if (a === b) return;
                if (this.sz[a] < this.sz[b]) [a, b] = [b, a];
                this.p[b] = a;
                this.sz[a] += this.sz[b];
            }
        }

        edges.sort((a, b) => a[2] - b[2]);

        let dsu = new DSU(V);
        let mst = 0, cnt = 0;
        let mstEdges = [];

        for (let [u, v, w] of edges) {
            if (!dsu.connected(u, v)) {
                dsu.unite(u, v);
                mst += w;
                cnt++;
                mstEdges.push([u, v, w]);
            }
        }

        if (cnt !== V - 1) return -1;

        let ans = Infinity;

        for (let [ru, rv, rw] of mstEdges) {
            let t = new DSU(V);
            let cur = 0, used = 0;

            for (let [u, v, w] of edges) {
                if ((u === ru && v === rv) || (u === rv && v === ru)) continue;

                if (!t.connected(u, v)) {
                    t.unite(u, v);
                    cur += w;
                    used++;
                }
            }

            if (used === V - 1 && cur > mst) ans = Math.min(ans, cur);
        }

        return ans === Infinity ? -1 : ans;
    }
}