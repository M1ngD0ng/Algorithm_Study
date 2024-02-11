import sys


T=int(sys.stdin.readline())
for _ in range(T):
  K=int(sys.stdin.readline())
  A=list(map(int,sys.stdin.readline().split()))
  dp=[[0]*K for _ in range(K)]

  for i in range(K-1):
    dp[i][i+1]=A[i]+A[i+1]

  for i in range(2,K+1):
    for j in range(K-i):
      k=j+i
      # dp[j][k]=min(dp[j][j]+dp[j+1][j+i],dp[j][j+i-1]+dp[j+i][j+i])
      dp[j][k]=min([dp[j][a]+dp[a+1][k] for a in range(j,k)])+sum(A[j:k+1])
  
  print(dp[0][K-1])