

// User function Template for Java

import java.util.HashMap;

class Solution {
    public int longestkSubstr(String s, int k) {
      HashMap<Character,Integer> set = new HashMap<>();
      
      int i = 0;
      int max = -1;
      int j= 1;
     set.put(s.charAt(i),1);
      while(j<s.length()){
          char ch = s.charAt(j);
          if(set.containsKey(ch)){
           int nf = set.get(ch) + 1;
           set.put(ch,nf);
          }else{
              if(set.size() == k){
                //  System.out.println(i+ " " + j);
                  max = Math.max(max,j-i);
                   while(set.size() == k){
                       if(set.get(s.charAt(i)) == 1){
                           set.remove(s.charAt(i));
                           i++;
                           break;
                       }else{
                           set.put(s.charAt(i),set.get(s.charAt(i))-1);
                       }
                       i++;
                   }
                
              }
            
              set.put(ch,1);
          }
          
         
          j++;
      }
       if(set.size() == k){
           max = Math.max(max,j-i);
          }
      return max;
      
    }
}