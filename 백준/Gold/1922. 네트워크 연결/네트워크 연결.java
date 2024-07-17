import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;


class Node implements Comparable<Node> {

    int cost;
    int from;
    int to;

    public Node(int cost, int from, int to) {
        this.cost = cost;
        this.from = from;
        this.to = to;
    }

    @Override
    public int compareTo(Node o) {
        return this.cost - o.cost;
    }
}

class Main {

    static int N, M, ans;
    static ArrayList<Node> cost = new ArrayList<>();
    static int[] parent;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        parent = new int[N + 1];
        StringTokenizer st;
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            cost.add(new Node(c, a, b));
        }
        Collections.sort(cost);

        for (Node n : cost) {
            int from = n.from;
            int to = n.to;

            if (find(from) != find(to)) {
                union(from, to);
                ans+=n.cost;
            }
        }
        System.out.println(ans);
    }

    public static int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public static void union(int a, int b) {
        a = find(a);
        b = find(b);

        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }
}