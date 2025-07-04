class Solution {
  public:
    int atMostK(vector<int> &nums, int k) {
        // code here
        int ans =0;
        vector<int> count(nums.size()+1);
        for (int l=0,r=0;r<nums.size(); r++){
            if (++count[nums[r]]==1)
                k--;
            while(k==-1) 
                if (--count[nums[l++]]==0)
                    k++;
            ans+=r-l+1;
        }
        return ans;
    }
};