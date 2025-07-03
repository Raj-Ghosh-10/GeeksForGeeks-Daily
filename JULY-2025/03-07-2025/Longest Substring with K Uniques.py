class Solution:
    def longestKSubstr(self, s, k):
        from collections import defaultdict
        cnt=defaultdict(int)
        left=0
        mx=-1
        for right in range(len(s)):
            ve=s[right]
            cnt[ve]+=1
            while len(cnt)>k:
                ve=s[left]
                cnt[ve]-=1
                if cnt[ve]==0:
                    cnt.pop(ve)
                left+=1
            if len(cnt)==k:
                mx=max(mx,right-left+1)
        return mx