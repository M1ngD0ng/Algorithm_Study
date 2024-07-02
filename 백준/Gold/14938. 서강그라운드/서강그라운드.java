import java.util.*;
import java.io.*;//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or


class Node implements Comparable<Node> {
    int end;
    int dist;

    public Node(int end, int dist) {
        this.end = end;
        this.dist = dist;
    }

    @Override
    public int compareTo(Node o) {
        return this.dist - o.dist;
    }
}

public class Main {
    static int N, M, R;
    static int[] item;
    static int ans;
    static ArrayList<ArrayList<Node>> map;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        ans = 0;
        item = new int[N+1];

        map = new ArrayList<>(N + 1);
        for (int i = 0; i < N + 1; i++) {
            map.add(new ArrayList<>());
        }


        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N+1; i++) {
            item[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());

            map.get(A).add(new Node(B, C));
            map.get(B).add(new Node(A, C));
        }
        for(int i=1;i<=N;i++){ 
            ans=Math.max(ans,dijkstra(i));
        }
        bw.write(String.valueOf(ans));
        bw.newLine();
        bw.flush();
    }

    public static int dijkstra(int start) {
        PriorityQueue<Node> q = new PriorityQueue<>();
        int[] distance = new int[N + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[start] = 0;
        q.offer(new Node(start, 0));

        while (!q.isEmpty()) {
            Node vNode = q.poll();
            if (distance[vNode.end] < vNode.dist) continue;

            for (Node node : map.get(vNode.end)) {
                int temp = vNode.dist + node.dist;
                if (temp >= distance[node.end] || temp > M) continue;
                distance[node.end] = temp;
                q.offer(new Node(node.end, temp));
            }
        }
        int res=0;
        for(int k=1;k<=N;k++){
            if(distance[k]<=M){
                res+=item[k];
            }
        }
        return res;
    }
}