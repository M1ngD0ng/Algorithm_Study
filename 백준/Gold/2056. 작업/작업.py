import sys
from collections import deque

N=int(sys.stdin.readline())
dp=[0 for _ in range(N+1)]

for i in range(1,N+1):
  temp=list(map(int,sys.stdin.readline().split()))
  dp[i]=temp[0]
  
  for j in temp[2:]:
    dp[i]=max(dp[i],dp[j]+temp[0])

print(max(dp))
