class Solution {
public:
    unordered_map<int, int> parent;
    int find(int x) {
        if(parent.find(x) == parent.end()) parent[x] = x;
        if(parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int x, int y) {
        int px = find(x);
        int py = find(y);
        if(px != py) parent[px] = py;
    }
    int maxRemove(vector<vector<int>>& stones) {
        for(auto &stone : stones) {
            unite(stone[0], stone[1] + 10001);
        }
        unordered_set<int> components;
        for(auto &stone : stones) {
            components.insert(find(stone[0]));
        }
        return stones.size() - components.size();
    }
};