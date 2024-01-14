import sys
from collections import deque

A,K=map(int,sys.stdin.readline().split())
def bfs():
  q=deque()
  q.append((A,0))

  dp=[1e8]*(K+1)
  dp[A]=0
  ans=1e8
  while q:
    v,cnt=q.popleft()
    if v==K:
      break
    dx=[1,v]

    for i in range(2):
      nx=v+dx[i]

      if nx>K:
        continue
      if dp[nx]>cnt+1:
        dp[nx]=cnt+1
        q.append((nx,cnt+1))
  print(dp[K])

bfs()