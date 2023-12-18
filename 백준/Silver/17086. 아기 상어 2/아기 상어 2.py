import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

A=[list(map(int,sys.stdin.readline().split())) for _ in range(N)] 

def bfs(x,y): 
  q=deque()
  q.append((x,y,0))
  dx=[1,0,-1,0,-1,-1,1,1]
  dy=[0,1,0,-1,-1,1,-1,1]
  visited=[[False]*M for _ in range(N)]
  visited[x][y]=True
  while q:
    vx,vy,c=q.popleft() 

    for i in range(8):
      nx=vx+dx[i]
      ny=vy+dy[i]
      if not (0<=nx<N and 0<=ny<M):
        continue
      if visited[nx][ny]:
        continue
      if A[nx][ny]==-1:
        A[x][y]=c+1
        return
      visited[nx][ny]=True
      q.append((nx,ny,c+1))

ans=0
for i in range(N):
  for j in range(M):
    if A[i][j]==1:
      A[i][j]=-1

for i in range(N):
  for j in range(M):
    if A[i][j]==-1:
      continue
    bfs(i,j)
  ans=max(ans,max(A[i])) 
print(ans)