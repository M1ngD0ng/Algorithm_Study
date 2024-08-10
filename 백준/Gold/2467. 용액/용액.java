import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());

        StringTokenizer st= new StringTokenizer(br.readLine());

        int[] A=new int[N];

        int ans=Integer.MAX_VALUE;

        int ix=-1;
        int iy=-1;
        boolean isSeparate=false;
        int point=-1;

        for(int i=0;i<N;i++){
            A[i]=Integer.parseInt(st.nextToken());
            if(i==0) continue;
            if(!isSeparate && (A[i-1]<0 && A[i]>0)) {
                isSeparate=true;
                point=i;
            }
            int temp=Math.abs(A[i]+A[i-1]);
            if(temp<ans){
                ans=temp;
                ix=i-1;
                iy=i;
            }
        }
        if(!isSeparate){
            System.out.println(A[ix]+" "+A[iy]);
            return;
        }

        int left=point-1;
        int right=point;

        while(true){
            int temp=A[left]+A[right];

            if(Math.abs(temp)<ans){
                ans=Math.abs(temp);
                ix=left;
                iy=right;
            }

            if(temp>0) left--;
            else if(temp<0) right++;
            else break;

            if(left==-1 || right==N) break;

        }

        System.out.println(A[ix]+" "+A[iy]);
    }
}