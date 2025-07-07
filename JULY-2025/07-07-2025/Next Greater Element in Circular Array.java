

// User Function Template for JAVA

import java.util.Stack;

class Solution{
    public static long[] nextLargerElement(long[] arr, int n) { 
        // Your code here
        Stack<Long> st = new Stack<>();
        long brr[] = new long[n];
        for(int i=2*n-1;i>=0;i--){
            while(st.size()>0 && st.peek()<=arr[i%n]){
                st.pop();
            }
            if(i<n){
                if(st.size()==0){
                    brr[i]=-1;
                }else{
                    brr[i]=st.peek();
                }
            }
            st.push(arr[i%n]);
        }
        return brr;
    } 
}