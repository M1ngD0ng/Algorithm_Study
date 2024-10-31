
import java.sql.Array;
import java.util.*;
import java.io.*;

public class Main {
    static class Point implements Comparable<Point>{
        int x;
        int y;

        Point(int x, int y){
            this.x=x;
            this.y=y;
        }
        @Override
        public int compareTo(Point p){
            if(this.x>p.x) return 1;
            else if(this.x<p.x) return -1;
            else{
                if(this.y>p.y) return 1;
                else if(this.y<p.y) return -1;
                else return 0;
            }
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
        Collections.sort(arr);

        for(Point p: arr){
            System.out.println(p.x+" "+p.y);
        }


    }
}