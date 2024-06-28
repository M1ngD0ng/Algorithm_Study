import java.util.*;
import java.io.*;//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or


// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static int V,E;
    static ArrayList<Edge> cost;
    static int[] parent;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        V=Integer.parseInt(st.nextToken());
        E=Integer.parseInt(st.nextToken());

        cost = new ArrayList<>(E);
        parent = new int[V+1];
        for (int i=0;i<V+1;i++){
            parent[i]=i;
        }

        for(int i=0;i<E;i++){
            st=new StringTokenizer(br.readLine());
            int A=Integer.parseInt(st.nextToken());
            int B=Integer.parseInt(st.nextToken());
            int C=Integer.parseInt(st.nextToken());

            cost.add(new Edge(A,B,C));
        }
        Collections.sort(cost);

        int ans=0;

        for(int i=0;i<cost.size();i++){
            int a=cost.get(i).from;
            int b=cost.get(i).to;
            int c=cost.get(i).weight;
            if(find(a)!=find(b)){
                ans+=c;
                union(a,b);
            }
        }
        bw.write(String.valueOf(ans));
        bw.flush();
    }
    static class Edge implements Comparable<Edge>{
        int from;
        int to;
        int weight;

        public Edge(int from, int to, int weight){
            this.from =from;
            this.to=to;
            this.weight=weight;
        }
        @Override
        public int compareTo(Edge o){
            return this.weight - o.weight;
        }
    }
    public static int find(int x){
        if(parent[x]!=x){
            parent[x]=find(parent[x]);
        }
        return parent[x];
    }
    public static void union(int a, int b){
        a= find(a);
        b=find(b);
        if(a<b) parent[b]=a;
        else parent[a]=b;
    }
}