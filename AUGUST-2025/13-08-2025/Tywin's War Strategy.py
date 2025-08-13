class Solution:
    def minSoldiers(self, arr, k):
        c=0 
        n=len(arr)
        n=n//2+1 if n%2 else n//2
        res=[]
        for i in range(len(arr)):
            if arr[i]%k==0:
                c+=1 
                res.append(0)
            else:
                res.append(k-arr[i]%k)

        res.sort()

        i=0
        sm=0
        while n>c:
            if res[i]:
                c+=1
                sm+=res[i]
            i+=1
        return sm