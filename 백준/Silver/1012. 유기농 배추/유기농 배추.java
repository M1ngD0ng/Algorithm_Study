import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node{
    int vx;
    int vy;

    public Node(int vx,int vy){
        this.vx=vx;
        this.vy=vy;
    }
}
class Main {

    static int T;
    static int M, N, K;

    static boolean[][] graph;
    static boolean[][] visited;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            graph = new boolean[N][M];
            visited=new boolean[N][M];
            int ans=0;

            for (int j = 0; j < K; j++) {
                st = new StringTokenizer(br.readLine());
                int Y=Integer.parseInt(st.nextToken());
                int X=Integer.parseInt(st.nextToken());
                graph[X][Y]=true;
            }

            for(int a=0;a<N;a++){
                for(int b=0;b<M;b++){
                    if(graph[a][b] && !visited[a][b]){
                        bfs(a,b);
                        ans++;
                    }
                }
            }
            System.out.println(ans);
        }
    }
    public static void bfs(int x, int y){
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(x,y));
        visited[x][y]=true;

        while(!q.isEmpty()){
            Node node = q.poll();

            for(int k=0;k<4;k++){
                int nx=dx[k]+node.vx;
                int ny=dy[k]+node.vy;

                if(!(0<=nx && nx<N && 0<=ny && ny<M)) continue;
                if(visited[nx][ny]) continue;
                visited[nx][ny]=true;
                if(graph[nx][ny]) q.offer(new Node(nx,ny));
            }
        }
    }
}