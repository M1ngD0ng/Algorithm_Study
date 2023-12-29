import sys
from collections import deque

N,K=map(int,sys.stdin.readline().split())
mm=max(N,K)
visited=[False]*(100001)
dp=[0]*(100001)

ans=[]
def bfs():
  q=deque()
  q.append((N,0))
  dx=[0,-1,1]
  while q: 
    v,cnt=q.popleft()
    if v==K:
      return cnt
    for i in range(3):
      c=0
      if i==0:
        nx=v*2
        c=cnt
      else:
        nx=v+dx[i]
        c=cnt+1
      if 0<=nx<=100000:
        if not visited[nx]:
          visited[nx]=True
          dp[nx]=c
          q.append((nx,c))
        elif dp[nx]>(cnt+1):
          dp[nx]=cnt+1
          q.append((nx,cnt+1))

print(bfs())