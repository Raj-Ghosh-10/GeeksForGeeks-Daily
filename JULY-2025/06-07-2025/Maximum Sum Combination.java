

// User function Template for Java

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    static List<Integer> maxCombinations(int N, int K, int A[], int B[]) 
    {
        List<Integer> list=new ArrayList<>();
        Arrays.sort(A);
        Arrays.sort(B);
        PriorityQueue<Integer> pq=new PriorityQueue<>();
    
    for(int i=N-1;i>N-1-K;i--)
    {
        for(int j=N-1;j>N-1-K;j--)
        {
            int sum=A[i]+B[j];
            
            if(pq.size()<K)
            {
                pq.add(sum);
            }
            else if(sum>pq.peek())
            {
                pq.poll();
                pq.add(sum);
            }
            else
            break;
        }
    }
    
    while(pq.size()>0&K>0)
    {
        list.add(0,pq.poll());
    }
    
    return list;
    }
}