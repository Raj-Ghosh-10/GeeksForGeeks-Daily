class Solution {
    public int minCost(string s, string t, char[,] transform, int[] cost) {
        const int INF = 1000000000;
        int[,] dist = new int[26, 26];
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                dist[i, j] = (i == j ? 0 : INF);
            }
        }
        int m = cost.Length;
        for (int i = 0; i < m; i++) {
            int u = transform[i, 0] - 'a';
            int v = transform[i, 1] - 'a';
            dist[u, v] = Math.Min(dist[u, v], cost[i]);
        }
        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                if (dist[i, k] == INF) continue;
                for (int j = 0; j < 26; j++) {
                    if (dist[k, j] == INF) continue;
                    int newCost = dist[i, k] + dist[k, j];
                    if (newCost < dist[i, j]) {
                        dist[i, j] = newCost;
                    }
                }
            }
        }
        long total = 0;
        for (int i = 0; i < s.Length; i++) {
            int a = s[i] - 'a';
            int b = t[i] - 'a';
            if (a == b) continue;
            int best = INF;
            for (int c = 0; c < 26; c++) {
                if (dist[a, c] < INF && dist[b, c] < INF) {
                    best = Math.Min(best, dist[a, c] + dist[b, c]);
                }
            }
            if (best == INF) return -1;
            total += best;
        }
        return (int)total;
    }
}