class Solution:
    def safeNodes(self, V, edges):
        from collections import deque
        revGraph = [[] for _ in range(V)]
        outdeg = [0] * V
        for u, v in edges:
            revGraph[v].append(u)
            outdeg[u] += 1
        q = deque()
        safe = []
        for i in range(V):
            if outdeg[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            safe.append(node)
            for parent in revGraph[node]:
                outdeg[parent] -= 1
                if outdeg[parent] == 0:
                    q.append(parent)
        safe.sort()
        return safe