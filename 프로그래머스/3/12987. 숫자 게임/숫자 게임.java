import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        Arrays.sort(A);
        Arrays.sort(B);
        
        int N=A.length;
        
        int temp=N-1;
        for(int i=N-1;i>=0;i--){
            if(temp<0) break;
            for(int j=temp;j>=0;j--){
                if(B[j]>A[i]){
                    temp=j-1;
                    answer++;
                    break;
                }
            }
        }
        return answer;
    }
}