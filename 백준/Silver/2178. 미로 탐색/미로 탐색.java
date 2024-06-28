import java.util.*;
import java.io.*;//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or

// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static int[] dx={0,0,-1,1};
    static int[] dy={1,-1,0,0};
    static int N,M;
    static int[][] graph;
    static int ans;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        graph = new int[N][M];
        ans=Integer.MAX_VALUE;

        for(int i=0;i<N;i++){
            String s = br.readLine();
            for(int j=0;j<M;j++){
                graph[i][j]=s.charAt(j)-'0';
            }
        }
        bfs(0,0);

        bw.write(String.valueOf(ans));
        bw.flush();
    }
    public static void bfs(int x, int y){
        boolean[][] visited= new boolean[N][M];
        Queue<int[]> q = new LinkedList<>();
        visited[x][y]=true;
        q.offer(new int[] {x,y,1});

        while(!q.isEmpty()){
            int[] v=q.poll();
            int vx=v[0];
            int vy=v[1];
            int cnt=v[2];

            if(vx==(N-1) && vy==(M-1)){
                ans=Math.min(ans,cnt);
            }
            for(int k=0;k<4;k++){
                int nx=vx+dx[k];
                int ny=vy+dy[k];

                if(nx<0 || ny<0 || nx>=N || ny>=M) continue;
                if(visited[nx][ny] || graph[nx][ny]==0) continue;
                visited[nx][ny]=true;
                q.offer(new int[] {nx,ny,cnt+1});
            }
        }

    }
}