import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.StringTokenizer;

class Node{
    long x;
    long y;

    Node(long x, long y){
        this.x=x;
        this.y=y;
    }
}

class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N=Integer.parseInt(br.readLine());

        ArrayList<Node> A=new ArrayList<>(N);

        st=new StringTokenizer(br.readLine());
        long xx=Integer.parseInt(st.nextToken());
        long yy=Integer.parseInt(st.nextToken());

        A.add(new Node(xx,yy));
        for(int i=0;i<N-1;i++){
            st=new StringTokenizer(br.readLine());
            long x=Integer.parseInt(st.nextToken());
            long y=Integer.parseInt(st.nextToken());

            A.add(new Node(x,y));
        }

        A.add(new Node(xx,yy));

        long a=0;
        long b=0;

        for(int i=0;i<N;i++){
            Node node1 = A.get(i);
            Node node2 = A.get(i+1);
            a+=(node1.x*node2.y);
            b+=(node1.y*node2.x);
        }
        double ans =Math.abs(a-b)*0.5;
        System.out.printf("%.1f", ans);
    }
}