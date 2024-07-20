import java.io.*;
import java.util.*;

class Node{
    int x;
    int y;

    public Node(int x, int y){
        this.x=x;
        this.y=y;
    }
}
class Main{

    static int M,N;
    static int[][] graph;
    static boolean[][] visited;
    static int tomato;
    static Queue<Node> q=new LinkedList<>();
    static int ans;
    static int[] dx={1,-1,0,0};
    static int[] dy={0,0,-1,1};

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        M=Integer.parseInt(st.nextToken());
        N=Integer.parseInt(st.nextToken());

        graph=new int[N][M];
        visited=new boolean[N][M];
        tomato=0;

        ans=0;

        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<M;j++){
                graph[i][j]=Integer.parseInt(st.nextToken());
                if(graph[i][j]==0) tomato++;
                else if(graph[i][j]==1) {
                    graph[i][j]=0;
                    visited[i][j]=true;
                    q.offer(new Node(i,j));
                }else visited[i][j]=true;
            }
        } 
        while(!q.isEmpty()){
            Node node = q.poll();
            int vx=node.x;
            int vy=node.y;

            for(int i=0;i<4;i++){
                int nx=dx[i]+vx;
                int ny=dy[i]+vy;

                if(nx<0 || nx>=N || ny<0 || ny>=M) continue;
                if(visited[nx][ny]) continue;
                if(graph[nx][ny]<=(graph[vx][vy]+1) && graph[nx][ny]!=0) continue;
                if(graph[nx][ny]==0) tomato--;
                visited[nx][ny]=true;
                graph[nx][ny]=graph[vx][vy]+1;
                q.offer(new Node(nx,ny));
            }
        }
        if (tomato != 0) {
            System.out.println(-1);
        } else{
            for(int i=0;i<N;i++){
                for(int j=0;j<M;j++){
                    ans=Math.max(ans,graph[i][j]);
                }
            }
            System.out.println(ans);
        }

    }
}