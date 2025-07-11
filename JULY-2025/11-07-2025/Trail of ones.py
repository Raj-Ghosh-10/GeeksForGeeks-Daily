class Solution:
    def countConsec(self, n: int) -> int:
        total = 1 << n 

        tmp1, tmp2 = 1, 2
        for i in range(2, n+1):
            tmp1, tmp2 = tmp2, tmp1 + tmp2
        return total - tmp2