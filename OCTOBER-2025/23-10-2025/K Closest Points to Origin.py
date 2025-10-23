import heapq,math
class Solution:
    def kClosest(self, points, k):
        # code here
        hp= []
        heapq.heapify(hp)
        cnt =0
        for i in range(len(points)):
            heapq.heappush(hp,(-math.sqrt(points[i][0]**2+points[i][1]**2),points[i]))
            cnt+=1
            if cnt>k:
                heapq.heappop(hp)
                cnt-=1
        res= []
        for i,j in hp:
            res.append(j)
        return res