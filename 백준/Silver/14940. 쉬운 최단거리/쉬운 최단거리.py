import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split()) 
A=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
tx,ty=0,0
for i in range(N):
  for j in range(M):
    if A[i][j]==2:
      tx,ty=i,j
      A[i][j]=0
      break

visited=[[False]*M for _ in range(N)]
def bfs():
  q=deque()
  q.append((tx,ty,0))
  visited[tx][ty]=True
  dx,dy=[1,0,-1,0],[0,1,0,-1]
  while q:
    vx,vy,c=q.popleft()

    for i in range(4):
      nx=vx+dx[i]
      ny=vy+dy[i]
      if not (0<=nx<N and 0<=ny<M):
        continue
      if visited[nx][ny]:
        continue
      if A[nx][ny]==0:
        visited[nx][ny]=True
        continue
      visited[nx][ny]=True
      A[nx][ny]=c+1
      q.append((nx,ny,c+1))


bfs()
for i in range(N):
  for j in range(M):
    if visited[i][j]:
      sys.stdout.write(str(A[i][j])+' ')
    else:
      if A[i][j]==0:
        sys.stdout.write(str(0)+' ')
      else:
        sys.stdout.write(str(-1)+' ')
  print()