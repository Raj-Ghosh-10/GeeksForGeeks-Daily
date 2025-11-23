import java.util.*;

class Solution {
    Map<Integer, Integer> parent = new HashMap<>();
    
    private int find(int x) {
        if (!parent.containsKey(x)) parent.put(x, x);
        if (parent.get(x) != x) parent.put(x, find(parent.get(x)));
        return parent.get(x);
    }
    
    private void union(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px != py) parent.put(px, py);
    }
    
    public int maxRemove(int[][] stones) {
        for (int[] stone : stones) {
            union(stone[0], stone[1] + 10001);
        }
        
        Set<Integer> components = new HashSet<>();
        for (int[] stone : stones) {
            components.add(find(stone[0]));
        }
        
        return stones.length - components.size();
    }
}