import sys

A=list(sys.stdin.readline().rstrip())
B=list(sys.stdin.readline().rstrip())
N,M=len(A),len(B)
dp=[[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i-1]==B[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
ans=0
for i in range(1,N+1):
  ans=max(ans,max(dp[i]))

print(ans)