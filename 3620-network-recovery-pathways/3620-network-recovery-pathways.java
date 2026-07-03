import java.util.*;

class Solution {

    static class Edge {
        int to;
        int cost;

        Edge(int t, int c) {
            to = t;
            cost = c;
        }
    }

    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {

        int n = online.length;

        List<Edge>[] graph = new ArrayList[n];
        int[] indegree = new int[n];

        for (int i = 0; i < n; i++)
            graph[i] = new ArrayList<>();

        int maxEdge = 0;

        for (int[] e : edges) {
            graph[e[0]].add(new Edge(e[1], e[2]));
            indegree[e[1]]++;
            maxEdge = Math.max(maxEdge, e[2]);
        }

        // Topological Sort
        List<Integer> topo = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < n; i++)
            if (indegree[i] == 0)
                q.offer(i);

        while (!q.isEmpty()) {
            int u = q.poll();
            topo.add(u);

            for (Edge e : graph[u]) {
                indegree[e.to]--;
                if (indegree[e.to] == 0)
                    q.offer(e.to);
            }
        }

        int lo = 0;
        int hi = maxEdge;
        int ans = -1;

        while (lo <= hi) {

            int mid = lo + (hi - lo) / 2;

            if (can(mid, graph, topo, online, k, n)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        return ans;
    }

    private boolean can(int minEdge,
                        List<Edge>[] graph,
                        List<Integer> topo,
                        boolean[] online,
                        long k,
                        int n) {

        long INF = Long.MAX_VALUE / 4;

        long[] dist = new long[n];
        Arrays.fill(dist, INF);

        dist[0] = 0;

        for (int u : topo) {

            if (dist[u] == INF)
                continue;

            if (u != 0 && u != n - 1 && !online[u])
                continue;

            for (Edge e : graph[u]) {

                if (e.cost < minEdge)
                    continue;

                int v = e.to;

                if (v != n - 1 && !online[v])
                    continue;

                if (dist[v] > dist[u] + e.cost) {
                    dist[v] = dist[u] + e.cost;
                }
            }
        }

        return dist[n - 1] <= k;
    }
}