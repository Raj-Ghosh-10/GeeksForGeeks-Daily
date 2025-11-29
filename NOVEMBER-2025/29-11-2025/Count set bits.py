class Solution:
    def countSetBits(self, n):
        count = 0
        while n > 0:
            x = n.bit_length() - 1  # position of MSB
            if x == 0:
                count += 1
                break
            count += x * (1 << (x - 1))
            count += n - (1 << x) + 1
            n -= (1 << x)
        return count