class Solution:
    def findOrder(self, n, prerequisites):
        from collections import deque
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for course, req in prerequisites:
            adj[req].append(course)
            indegree[course] += 1
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        order = []
        while q:
            course = q.popleft()
            order.append(course)
            for nxt in adj[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return order if len(order) == n else []