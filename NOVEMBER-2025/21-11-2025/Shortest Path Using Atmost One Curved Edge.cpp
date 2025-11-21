class Solution {
public:
    const long long INF = 1e18;
    vector<long long> dijkstra(int V, int src, vector<vector<pair<int,int>>>& adj){
        vector<long long> dist(V, INF);
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
        dist[src] = 0;
        pq.push({0, src});
        while(!pq.empty()){
            auto [d, u] = pq.top(); pq.pop();
            if(d != dist[u]) continue;
            for(auto &p: adj[u]){
                int v = p.first, w = p.second;
                if(dist[v] > d + w){
                    dist[v] = d + w;
                    pq.push({dist[v], v});
                }
            }
        }
        return dist;
    }

    int shortestPath(int V, int a, int b, vector<vector<int>> &edges) {
        vector<vector<pair<int,int>>> adj(V);
        for(auto &e : edges){
            int u = e[0], v = e[1], w1 = e[2];
            adj[u].push_back({v, w1});
            adj[v].push_back({u, w1});
        }
        vector<long long> distA = dijkstra(V, a, adj);
        vector<long long> distB = dijkstra(V, b, adj);
        long long ans = distA[b];
        for(auto &e : edges){
            int u = e[0], v = e[1], w2 = e[3];
            if(distA[u] != INF && distB[v] != INF){
                ans = min(ans, distA[u] + w2 + distB[v]);
            }
            if(distA[v] != INF && distB[u] != INF){
                ans = min(ans, distA[v] + w2 + distB[u]);
            }
        }
        return ans >= INF ? -1 : (int)ans;
    }
};