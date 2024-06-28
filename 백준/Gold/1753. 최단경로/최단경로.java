import java.util.*;
import java.io.*;//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or

class Node {
    int end;
    int weight;

    public Node(int end, int weight) {
        this.end = end;
        this.weight = weight;
    }
}

class Next implements Comparable<Next>{
    int distance;
    int node;

    public Next(int distance, int node){
        this.distance=distance;
        this.node=node;
    }
    @Override
    public int compareTo(Next o){
        return Integer.compare(this.distance, o.distance);
    }
}
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static int V, E, K;
    static List<Node>[] map;
    static int[] dist;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        K = Integer.parseInt(br.readLine());

        map = new List[V + 1];
        dist = new int[V+1];
        Arrays.fill(dist,Integer.MAX_VALUE);

        for (int i = 1; i < V+1; i++) {
            map[i] = new ArrayList<>();
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());

            map[A].add(new Node(B, C));
        }
        dijkstra(K);
        for(int i=1;i<V+1;i++){
            if(dist[i]==Integer.MAX_VALUE) bw.write("INF\n");
            else{
                bw.write(String.valueOf(dist[i]));
                bw.newLine();
            }
        }
        bw.flush();
    }

    public static void dijkstra(int start) {
        PriorityQueue<Next> pQ = new PriorityQueue<>();
        dist[start]=0;

        Next next = new Next(0,start);
        pQ.offer(next);

        while(!pQ.isEmpty()){
            Next vNext = pQ.poll();

            for(int x=0;x<map[vNext.node].size();x++){
                int nextNode = map[vNext.node].get(x).end;
                int nextWeight = map[vNext.node].get(x).weight;

                if((vNext.distance+nextWeight)>dist[nextNode]) continue;
                dist[nextNode]=vNext.distance+nextWeight;

                next = new Next(dist[nextNode], nextNode);
                pQ.offer(next);
            }
        }
    }
}