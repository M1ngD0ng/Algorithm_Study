import sys


N,K=map(int,sys.stdin.readline().split())
A=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dp=[[0]*(K+1) for _ in range(N+1)]
 

for i in range(1,N+1):
  for j in range(K+1):
    if j>=A[i-1][0]:
      dp[i][j]=max(dp[i-1][j],dp[i-1][j-A[i-1][0]]+A[i-1][1])
    else:
      dp[i][j]=dp[i-1][j]

print(max(dp[N]))