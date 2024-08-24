import java.util.*;

class Solution {
    public int solution(int m, int n, int[][] A) {
        int answer = 0;
        int[][] dp=new int[n][m];
        int[] dx={-1,0};
        int[] dy={0,-1};
        
        Arrays.stream(A).forEach(a->dp[a[1]-1][a[0]-1]=-1);
        
        dp[0][0]=1;
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(dp[i][j]==-1 || (i==0 && j==0)) continue;
                
                for(int k=0;k<2;k++){
                    int nx=i+dx[k];
                    int ny=j+dy[k];
                    
                    if(nx<0 || ny<0 || dp[nx][ny]==-1) continue;
                    dp[i][j]+=dp[nx][ny];
                }
                dp[i][j]%=1000000007;
            }
        }
        
        return dp[n-1][m-1]%1000000007;
    }
}