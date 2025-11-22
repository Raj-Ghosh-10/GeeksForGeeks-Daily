class Solution:
    def minConnect(self, V, edges):
        parent = list(range(V))
        rank = [0] * V

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pb] < rank[pa]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1

        redundant = 0

        for u, v in edges:
            if find(u) == find(v):
                redundant += 1
            else:
                unite(u, v)

        components = sum(1 for i in range(V) if find(i) == i)
        need = components - 1

        return need if redundant >= need else -1