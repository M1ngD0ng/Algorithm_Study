import java.util.*;
import java.io.*;//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or

// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        int[] dp =new int[N];
        Arrays.fill(dp,1);

        for(int i=1;i<N;i++){
            for(int j=0;j<i;j++){
                if(arr[j]<arr[i]) dp[i]=Math.max(dp[j]+1, dp[i]);
            }
        }
        int cnt = Arrays.stream(dp).max().getAsInt();
        bw.write(String.valueOf(cnt));
        bw.newLine();
        ArrayList<Integer> res = new ArrayList<>();

        for(int i=N-1;i>=0;i--){
            if (dp[i]==cnt){
                res.add(arr[i]);
                cnt--;
            }
        }
        Collections.sort(res);
        for(int a: res){
            bw.write(String.valueOf(a)+" ");
        }

        bw.flush();


    }
}