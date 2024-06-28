import org.w3c.dom.Node;

import java.util.*;
import java.io.*;//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or

// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static int N, K;
    static int[][] map;
    static boolean[] visited;
    static int ans;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        map = new int[N][N];
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    map[i][j] = Math.min(map[i][j], map[i][k] + map[k][j]);
                }
            }
        }
        ans = Integer.MAX_VALUE;
        visited[K]=true;
        dfs(K, 1, 0);

        bw.write(String.valueOf(ans));
        bw.newLine();
        bw.flush();
    }

    public static void dfs(int node, int cnt, int sum) {
        if (cnt == N) {
            ans = Math.min(ans, sum);
        } else{
            for(int i=0;i<N;i++){
                if(visited[i]) continue;
                visited[i]=true;
                dfs(i,cnt+1, sum+map[node][i]);
                visited[i]=false;
            }
        }
    }
}