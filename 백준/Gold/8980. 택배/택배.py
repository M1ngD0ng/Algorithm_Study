import sys
from collections import defaultdict

N,C=map(int,sys.stdin.readline().split())
M=int(sys.stdin.readline())

A=[list(map(int,sys.stdin.readline().split())) for _ in range(M)]

A.sort(key=lambda x:(x[1]))
dp=[0]*(N+1)

ans=0
for i in range(M):
  pack=A[i][2]
  for j in range(A[i][0],A[i][1]):
    if dp[j]+pack>C:
      pack=C-dp[j]
  for j in range(A[i][0],A[i][1]):
    dp[j]+=pack
  ans+=pack
  
print(ans)