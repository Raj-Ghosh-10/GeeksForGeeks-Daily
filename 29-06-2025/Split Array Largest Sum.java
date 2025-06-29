class Solution {
    static int numberOfSubar(int []a, int maxSumInASingleAr){
        int num = 1;
        int s = 0;
        for(int i=0;i<a.length;i++){
            if(a[i]+s <= maxSumInASingleAr){
                s+=a[i];
            }else{
                num++;
                s = a[i];
            }
        }
        return num;
    }
    
    static int splitArray(int[] arr , int N, int K) {
        
        int sum = 0;
        int max = Integer.MIN_VALUE;
        
        for(int i: arr){
            sum += i;
            max = Math.max(max, i);
        }
        
        int low = max;
        int high = sum;
        
        while(low<=high){
            int mid = (low+high)/2;
            if(numberOfSubar(arr,mid)<=K){
                high = mid-1;
            }
            else
                low = mid+1;
        }
        return low;
    }
};