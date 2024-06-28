
import java.util.*;
import java.io.*;//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or

// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static int N, M;
    static List<ArrayList<Integer>> arr;
    static int[] inDegree;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new ArrayList<>(N+1);
        for (int i = 0; i < N+1; i++) {
            arr.add(new ArrayList<>());
        }
        inDegree = new int[N + 1];

        // ---초기 설정

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            arr.get(a).add(b);
            inDegree[b]++;
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i < N + 1; i++) {
            if (inDegree[i] == 0) q.offer(i);
        }

        while (!q.isEmpty()) {
            int v = q.poll();
            bw.write(String.valueOf(v)+" ");

            for (int i : arr.get(v)) {
                inDegree[i]--;
                if(inDegree[i]==0) q.offer(i);
            }
        }
        bw.flush();
    }
}