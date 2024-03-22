import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())
A=[ list(sys.stdin.readline().rstrip()) for _ in range(N)]

xy=[]
for i in range(N):
  for j in range(M):
    if A[i][j]=='o':
      xy.append([i,j])


def bfs():
  ans=1e8
  q=deque()
  q.append((xy[0][0],xy[0][1],xy[1][0],xy[1][1],0))
  d=set()
  d.add((xy[0][0],xy[0][1],xy[1][0],xy[1][1]))
  dx,dy=[1,-1,0,0],[0,0,1,-1]

  while q:
    x1,y1,x2,y2,cnt=q.popleft() 
    for i in range(4):
      nx1,nx2=dx[i]+x1,dx[i]+x2
      ny1,ny2=dy[i]+y1,dy[i]+y2
      
      if not (0<=nx1<N and 0<=ny1<M):
        if 0<=nx2<N and 0<=ny2<M:
          ans=min(ans,cnt+1) 
        continue
      elif not (0<=nx2<N and 0<=ny2<M):
        ans=min(ans,cnt+1) 
        continue
      if A[nx1][ny1]=='#':
        nx1,ny1=x1,y1
      if A[nx2][ny2]=='#':
        nx2,ny2=x2,y2
      if (nx1,ny1,nx2,ny2) in d:
        continue
      d.add((nx1,ny1,nx2,ny2))
      
      q.append((nx1,ny1,nx2,ny2,cnt+1))
  if ans>10:
    return -1
  return ans



print(bfs())