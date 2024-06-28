import java.util.*;
import java.io.*;//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or

// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static int N, M;
    static ArrayList<ArrayList<Integer>> parent;
    static ArrayList<ArrayList<Integer>> child;
    static int X, Y;
    static boolean[] visited;
    static int ans;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer sr;
        N = Integer.parseInt(br.readLine());
        parent = new ArrayList<ArrayList<Integer>>(N + 1);
        child = new ArrayList<ArrayList<Integer>>(N + 1);
        visited = new boolean[N + 1];
        ans = Integer.MAX_VALUE;

        for (int i = 0; i < N + 1; i++) {
            parent.add(new ArrayList<Integer>());
            child.add(new ArrayList<Integer>());
        }
        sr = new StringTokenizer(br.readLine());
        X = Integer.parseInt(sr.nextToken());
        Y = Integer.parseInt(sr.nextToken());

        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            sr = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(sr.nextToken());
            int B = Integer.parseInt(sr.nextToken());
            parent.get(B).add(A);
            child.get(A).add(B);
        }
        dfs(X, 0);
        if(ans==Integer.MAX_VALUE) bw.write(String.valueOf(-1));
        else bw.write(String.valueOf(ans));
        bw.flush();
    }

    public static void dfs(int node, int cnt) {
        if (node == Y) {
            ans = Math.min(ans, cnt);
        }
        for (int nextNode : parent.get(node)) {
            if (visited[nextNode]) continue;
            visited[nextNode] = true;
            dfs(nextNode, cnt+1);
        }
        for (int nextNode : child.get(node)) {
            if (visited[nextNode]) continue;
            visited[nextNode] = true;
            dfs(nextNode, cnt+1);
        }
    }

}