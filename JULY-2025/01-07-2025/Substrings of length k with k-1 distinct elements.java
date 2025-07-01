class Solution {
    public int substrCount(String s, int k) {
        Map<Character, Integer> map = new HashMap<>();
        int n = s.length();
        for(int i=0; i<k; i++) {
            char ch = s.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        int ans = 0;
        if(map.size() == k - 1) ans++;
        for(int i=k; i<n; i++) {
            char prev = s.charAt(i - k);
            char curr = s.charAt(i);
            map.put(curr, map.getOrDefault(curr, 0) + 1);
            map.put(prev, map.get(prev) - 1);
            if(map.get(prev) == 0) map.remove(prev);
            if(map.size() == k - 1) ans++;
        }
        return ans;
    }
}