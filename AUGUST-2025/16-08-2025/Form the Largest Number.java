

//User function Template for Java

class Solution {
    String printLargest(int n, String[] nums) {
        // code here
        Arrays.sort(nums,new Comparator<String>(){
            @Override
            public int compare(String a,String b){
                String str1=a+b;
                String str2=b+a;
                return str2.compareTo(str1);
            }
        }
        );
        
        if(nums[0].equals("0")){
            return "0";
        }
        StringBuilder sb=new StringBuilder();
        
        for(String num:nums){
            sb.append(num);
        }
        return sb.toString();
    }
}