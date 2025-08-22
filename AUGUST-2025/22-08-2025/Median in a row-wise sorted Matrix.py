class Solution:
    def median(self, mat):
        # code here 
        arr = []
        for i in mat:
            for j in i:
                arr.append(j)
        arr.sort()
        k = len(arr)
        return arr[(k//2)]
        