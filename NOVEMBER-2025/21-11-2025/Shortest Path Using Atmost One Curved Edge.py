import heapq

class Solution:
    def dijkstra(self, V, src, adj):
        INF = 10**18
        dist = [INF] * V
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

    def shortestPath(self, V, a, b, edges):
        INF = 10**18
        adj = [[] for _ in range(V)]

        for u, v, w1, w2 in edges:
            adj[u].append((v, w1))
            adj[v].append((u, w1))

        distA = self.dijkstra(V, a, adj)
        distB = self.dijkstra(V, b, adj)

        ans = distA[b]

        for u, v, w1, w2 in edges:
            if distA[u] < INF and distB[v] < INF:
                ans = min(ans, distA[u] + w2 + distB[v])
            if distA[v] < INF and distB[u] < INF:
                ans = min(ans, distA[v] + w2 + distB[u])

        return -1 if ans >= INF else ans