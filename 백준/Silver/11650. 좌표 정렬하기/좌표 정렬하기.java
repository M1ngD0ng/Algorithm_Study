
import java.util.*;
import java.io.*;

public class Main {
    static class Point{
        int x;
        int y;

        Point(int x, int y){
            this.x=x;
            this.y=y;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());

        List<Point> arr = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int A=Integer.parseInt(st.nextToken());
            int B=Integer.parseInt(st.nextToken());

            arr.add(new Point(A,B));

        }
        arr.sort((a,b)-> {
            if(a.x==b.x) return Integer.compare(a.y, b.y);
            else return Integer.compare(a.x, b.x);
        });

        for(Point p: arr){
            System.out.println(p.x+" "+p.y);
        }


    }
}