class Solution {
    public List<int> findOrder(int n, int[,] prerequisites) {
        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++)
            adj[i] = new List<int>();
        int[] indegree = new int[n];
        int m = prerequisites.GetLength(0);
        for (int i = 0; i < m; i++) {
            int course = prerequisites[i, 0];
            int prereq = prerequisites[i, 1];
            adj[prereq].Add(course);
            indegree[course]++;
        }
        Queue<int> q = new Queue<int>();
        for (int i = 0; i < n; i++)
            if (indegree[i] == 0)
                q.Enqueue(i);
        List<int> order = new List<int>();
        while (q.Count > 0) {
            int curr = q.Dequeue();
            order.Add(curr);
            foreach (int next in adj[curr]) {
                indegree[next]--;
                if (indegree[next] == 0)
                    q.Enqueue(next);
            }
        }
        return (order.Count == n) ? order : new List<int>();
    }
}