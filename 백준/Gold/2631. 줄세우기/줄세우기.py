import sys

N=int(sys.stdin.readline())
A=[ int(sys.stdin.readline()) for _ in range(N)]
dp=[1]*N

for i in range(1,N):
  for j in range(i):
    if A[j]<A[i]:
      dp[i]=max(dp[i],dp[j]+1) 
print(N-max(dp))