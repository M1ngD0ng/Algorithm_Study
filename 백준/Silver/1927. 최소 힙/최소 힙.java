import java.util.*;
import java.io.*;//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or

// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pQ = new PriorityQueue<>();

        for(int i=0;i<N;i++){
            int x = Integer.parseInt(br.readLine());
            if(x==0){
                if(!pQ.isEmpty()){
                    bw.write(String.valueOf(pQ.poll()));
                    bw.newLine();
                }else {
                    bw.write("0\n");
                }
            }else{
                pQ.offer(x);
            }
        }
        bw.flush();
    }
}