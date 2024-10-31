 
import java.util.*;
import java.io.*;

public class Main {

    static class Time implements Comparable<Time> {
        int S;
        int T;

        Time(int S, int T) {
            this.S = S;
            this.T = T;
        }

        @Override
        public int compareTo(Time t) {
            if (this.S > t.S) return 1;
            else if (this.S < t.S) return -1;
            else {
                if ((this.T - this.S) > (t.T - t.S)) return 1;
                else if ((this.T - this.S) < (t.T - t.S)) return -1;
                else return 0;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());

        List<Time> arr = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            arr.add(new Time(A, B));
        }

        int ans = 0;
        Collections.sort(arr);

        PriorityQueue<Integer> pQ = new PriorityQueue<>();

        for (Time t : arr) {
            if (pQ.isEmpty()){
                pQ.add(t.T);
            }
            else {
                while (!pQ.isEmpty()) {
                    int temp = pQ.poll();
                    if (t.S < temp) {
                        pQ.add(temp);
                        break;
                    }
                }
                pQ.add(t.T);
            }
            ans=Math.max(ans, pQ.size());
        }

        System.out.println(ans);

    }
}