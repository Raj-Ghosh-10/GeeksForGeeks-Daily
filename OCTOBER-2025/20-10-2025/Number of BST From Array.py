class Solution:
    bsts=[1,1,2,5,14,42]
    def countBSTs(self, arr):
        # Code here
        n=len(arr)
        l=[]
        for i in range(n):
            x=0
            c=0
            for j in range(n):
                if arr[i]<arr[j]:
                    c+=1
                elif arr[i]>arr[j]:
                    x+=1
            l.append(self.bsts[x]*self.bsts[c])
        return l