import java.io.*;
import java.util.*;

public class Main {

    static class Edge {
        int to;
        int weight;

        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;

        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) {
                continue;
            }
            StringTokenizer st = new StringTokenizer(line);
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            List<Edge>[] graph = new ArrayList[n];
            for (int i = 0; i < n; i++) {
                graph[i] = new ArrayList<>();
            }

            int[] indegree = new int[n];
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int z = Integer.parseInt(st.nextToken());
                graph[x].add(new Edge(y, z));
                indegree[y]++;
            }

            int[] dist = new int[n];
            Arrays.fill(dist, 1);
            Queue<Integer> queue = new ArrayDeque<>();
            for (int i = 0; i < n; i++) {
                if (indegree[i] == 0) {
                    queue.offer(i);
                }
            }

            while (!queue.isEmpty()) {
                int node = queue.poll();

                for (Edge edge : graph[node]) {
                    int child = edge.to;
                    int weight = edge.weight;
                    dist[child] = Math.max(
                        dist[child],
                        dist[node] + weight
                    );
                    indegree[child]--;
                    if (indegree[child] == 0) {
                        queue.offer(child);
                    }
                }
            }

            int answer = 0;
            for (int i = 0; i < n; i++) {
                answer = Math.max(answer, dist[i]);
            }

            System.out.println(answer);
        }
    }
}