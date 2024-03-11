import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())
A=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]

def bfs():
  global ans
  q=deque()
  q.append((0,0,0,1))
  visited=[[[False]*2 for _ in range(M)] for _ in range(N)]
  visited[0][0][0]=True
  visited[0][0][1]=True

  dx,dy=[0,0,-1,1],[1,-1,0,0]

  while q:
    vx,vy,bk,cnt=q.popleft()

    if (vx,vy)==(N-1,M-1):
      print(cnt)
      return

    for k in range(4):
      nx=vx+dx[k]
      ny=vy+dy[k]

      if not (0<=nx<N and 0<=ny<M):
        continue
      if visited[nx][ny][bk]:
        continue
      if A[nx][ny]==0:
        visited[nx][ny][bk]=True
        q.append((nx,ny,bk,cnt+1))
      elif A[nx][ny]==1 and bk==0:
        visited[nx][ny][1]=True
        q.append((nx,ny,1,cnt+1))

  
  print(-1)
    
  
ans=1e8
bfs()
