from collections import deque, defaultdict

class Solution:
    def shortCycle(self, V, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = float('inf')

        for src in range(V):
            dist = [-1] * V
            parent = [-1] * V

            q = deque([src])
            dist[src] = 0

            while q:
                node = q.popleft()

                for nbr in adj[node]:
                    if dist[nbr] == -1:
                        dist[nbr] = dist[node] + 1
                        parent[nbr] = node
                        q.append(nbr)

                    elif parent[node] != nbr:
                        ans = min(ans, dist[node] + dist[nbr] + 1)

        return ans if ans != float('inf') else -1