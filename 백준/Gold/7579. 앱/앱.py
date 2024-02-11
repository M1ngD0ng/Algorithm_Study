import sys


N,M=map(int,sys.stdin.readline().split())
A=[0]+list(map(int,sys.stdin.readline().split()))
B=[0]+list(map(int,sys.stdin.readline().split()))
dp=[[0]*(sum(B)+1) for _ in range(N+1)]

ans=sum(B)
for i in range(1,N+1):
  for j in range(sum(B)+1):
    if j<B[i]:
      dp[i][j]=dp[i-1][j]
    else:
      dp[i][j]=max(dp[i-1][j-B[i]]+A[i],dp[i-1][j])
    
    if dp[i][j]>=M:
      ans=min(ans,j)
if M!=0:
  print(ans)
else:
  print(0)    
