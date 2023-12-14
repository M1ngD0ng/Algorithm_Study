import sys

T=int(sys.stdin.readline())
for _ in range(T):
  A=[[] for _ in range(2)]
  n=int(sys.stdin.readline())
  A[0]=list(map(int,sys.stdin.readline().split()))
  A[1]=list(map(int,sys.stdin.readline().split()))

  dp=[[0 for _ in range(n)] for _ in range(2)]
  dp[0][0]=A[0][0]
  dp[1][0]=A[1][0]
  if n==1:
    print(max(dp[0][0],dp[1][0]))
  else:
    for i in range(1,n):
      dp[0][i]=A[0][i]+dp[1][i-1]
      dp[1][i]=A[1][i]+dp[0][i-1]

      if i>1:
        for k in range(2):
          for x in range(2):
            if (dp[k][i-2]+A[x][i])>dp[x][i]:
              dp[x][i]=dp[k][i-2]+A[x][i]

    print(max(dp[0][n-1],dp[1][n-1]))
          

        
