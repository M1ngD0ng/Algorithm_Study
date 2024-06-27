import java.util.*;
import java.io.*;//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or

// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static int N, M;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        graph = new int[N][M];
        int cnt = 0;
        int ans = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        visited = new boolean[N][M];
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (visited[i][j] || graph[i][j] == 0) continue;
                visited[i][j] = true;
                cnt++;
                q.offer(new int[]{i, j});
                int temp = 0;
                while (!q.isEmpty()) {
                    temp++;
                    int[] xy = q.poll();
                    int x = xy[0];
                    int y = xy[1];

                    for (int k = 0; k < 4; k++) {
                        int nx = x + dx[k];
                        int ny = y + dy[k];

                        if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
                        if (visited[nx][ny] || graph[nx][ny] == 0) continue;

                        visited[nx][ny] = true;
                        q.offer(new int[]{nx, ny});
                    }
                }
                ans = Math.max(ans, temp);
            }
        }
        bw.write(String.valueOf(cnt));
        bw.newLine();
        bw.write(String.valueOf(ans));
        bw.flush();

    }
}