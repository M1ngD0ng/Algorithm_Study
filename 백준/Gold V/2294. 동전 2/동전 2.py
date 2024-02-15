import sys

N,K=map(int,sys.stdin.readline().split())
A=[0]
for _ in range(N):
  A.append(int(sys.stdin.readline()))
A.sort()

dp=[[1e8]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
  for j in range(1,K+1):
    if j%A[i]==0:
      dp[i][j]=min(dp[i][j],j//A[i])
    if j-A[i]>=0:
        dp[i][j]=min(dp[i][j],dp[i][j-A[i]]+1)
    dp[i][j]=min(dp[i-1][j],dp[i][j])
 
if dp[N][K]>=1e8:
  print(-1)
else:
  print(dp[N][K])