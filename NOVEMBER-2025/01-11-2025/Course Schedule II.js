class Solution {
    findOrder(n, prerequisites) {
        const adj = Array.from({ length: n }, () => []);
        const indegree = Array(n).fill(0);
        for (let [course, prereq] of prerequisites) {
            adj[prereq].push(course);
            indegree[course]++;
        }
        const queue = [];
        for (let i = 0; i < n; i++) {
            if (indegree[i] === 0) queue.push(i);
        }
        const order = [];
        while (queue.length > 0) {
            const curr = queue.shift();
            order.push(curr);
            for (let next of adj[curr]) {
                indegree[next]--;
                if (indegree[next] === 0) queue.push(next);
            }
        }
        return order.length === n ? order : [];
    }
}