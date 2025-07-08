import java.util.HashMap;

class solver
{
    static int[] print_next_greater_freq(int arr[], int n)
    {
         HashMap<Integer, Integer> map= new HashMap<>();
        
        for(int i=0;i<n;i++){
            map.put(arr[i], map.getOrDefault(arr[i], 0)+1);
        }
        
        int max=0;
        int[] freq= new int[n];
        for(int i=0;i<n;i++){
            freq[i] = map.get(arr[i]);
            max= Math.max(max, map.get(arr[i]));
        }
        
        int[] ans= new int[n];
        int i=0, j=1;
        while(i<n && j<n+1){
            if(freq[i]==max || j==n){
                ans[i] = -1;
                i++;
                j=i+1;
            }
            else if(freq[i]<freq[j]){
                ans[i]= arr[j];
                i++;
                j=i+1;
            }
            
            else j++;
        }
        ans[n-1]= -1;
        
        return ans;
    }
}