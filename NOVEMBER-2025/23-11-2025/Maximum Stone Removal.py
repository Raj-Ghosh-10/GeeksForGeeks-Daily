class Solution:
    def maxRemove(self, stones):
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for x, y in stones:
            union(x, y + 10001)

        components = set()
        for x, y in stones:
            components.add(find(x))

        return len(stones) - len(components)