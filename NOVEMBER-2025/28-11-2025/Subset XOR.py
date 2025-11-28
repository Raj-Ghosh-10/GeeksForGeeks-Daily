class Solution:
    def subsetXOR(self, n: int):
        ans = []
        totalXOR = 0
        for i in range(1, n + 1):
            totalXOR ^= i
        if totalXOR == n:
            ans = list(range(1, n + 1))
        else:
            x = totalXOR ^ n
            ans = [i for i in range(1, n + 1) if i != x]
        return ans