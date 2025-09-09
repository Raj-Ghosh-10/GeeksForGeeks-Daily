class Solution:
    def assignHole(self, mices, holes):
        # code here
        return max(abs(a-b) for a, b in zip(sorted(mices), sorted(holes)))