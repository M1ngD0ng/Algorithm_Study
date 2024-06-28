import java.util.*;
import java.io.*;//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or


// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());

        Set<String> setStr = new HashSet<>();
        for(int i =0;i<N;i++){
            String s = br.readLine();
            setStr.add(s);
        }
        int cnt=0;
        for(int i=0;i<M;i++){
            String s= br.readLine();
            if(setStr.contains(s)) cnt++;
        }
        bw.write(String.valueOf(cnt));
        bw.flush();

    }
}