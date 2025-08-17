class Solution:
    def rearrange(self, arr, m):
        arr.sort(key=lambda x:abs(x-m))
        return arr