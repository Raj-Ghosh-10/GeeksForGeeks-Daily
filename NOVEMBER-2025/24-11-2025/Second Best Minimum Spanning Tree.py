class Solution:
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def connected(self, a, b):
            return self.find(a) == self.find(b)

        def unite(self, a, b):
            a = self.find(a)
            b = self.find(b)
            if a == b:
                return
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]

    def secondMST(self, V, edges):
        # edges: list of [u, v, w]
        
        # Sort edges by weight
        e = sorted(edges, key=lambda x: x[2])

        dsu = self.DSU(V)
        mstWeight = 0
        mstEdges = 0
        
        # store MST edges
        mstEdgesList = []

        # Build MST using Kruskal
        for u, v, w in e:
            if not dsu.connected(u, v):
                dsu.unite(u, v)
                mstWeight += w
                mstEdges += 1
                mstEdgesList.append((u, v, w))

        # If MST not possible
        if mstEdges != V - 1:
            return -1

        secondBest = float('inf')

        # Try removing each MST edge
        for remU, remV, remW in mstEdgesList:
            temp = self.DSU(V)
            curWeight = 0
            cnt = 0

            for u, v, w in e:

                # Must skip both (u == remU and v == remV) AND (u == remV and v == remU)
                if (u == remU and v == remV) or (u == remV and v == remU):
                    continue

                if not temp.connected(u, v):
                    temp.unite(u, v)
                    curWeight += w
                    cnt += 1

            # Valid spanning tree and strictly > MST weight
            if cnt == V - 1 and curWeight > mstWeight:
                secondBest = min(secondBest, curWeight)

        return -1 if secondBest == float('inf') else secondBest