class Solution:
    def subsetXORSum(self, arr):
        n = len(arr)
        ans = 0
        for bit in range(11):
            countSet = sum(1 for num in arr if num & (1 << bit))
            if countSet > 0:
                ans += (1 << bit) * (1 << (n - 1))

        return ans