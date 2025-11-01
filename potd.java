class Solution {
    public ArrayList<Integer> findOrder(int n, int[][] prerequisites) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        int[] indegree = new int[n];
        for(int[] pre : prerequisites) {
            int course = pre[0];
            int req = pre[1];
            adj.get(req).add(course);
            indegree[course]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i < n; i++) {
            if(indegree[i] == 0) q.add(i);
        }
        ArrayList<Integer> order = new ArrayList<>();
        while(!q.isEmpty()) {
            int curr = q.poll();
            order.add(curr);
            for(int next : adj.get(curr)) {
                indegree[next]--;
                if(indegree[next] == 0) q.add(next);
            }
        }
        if(order.size() == n) return order;
        return new ArrayList<>();
    }
}