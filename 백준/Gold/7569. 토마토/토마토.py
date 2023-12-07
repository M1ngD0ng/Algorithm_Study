import sys
from collections import deque
sys.setrecursionlimit(10**6)
M,N,H=map(int,sys.stdin.readline().split())
graph=[ [list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

visited=[ [[False]*M for _ in range(N)] for _ in range(H)]

for k in range(H):
 for i in range(N):
   for j in range(M):
     if graph[k][i][j]==-1:
       visited[k][i][j]=True


def inRange(nz,nx,ny):
  return 0<=nz<H and 0<=nx<N and 0<=ny<M



day=0
def bfs(q):
  global day
  cnt=0
  dx=[0,0,1,0,-1,0]
  dy=[0,0,0,1,0,-1]
  dz=[1,-1,0,0,0,0]
  q2=deque()
  
  while q:
    vz,vx,vy=q.popleft()
    visited[vz][vx][vy]=True
    
    for i in range(6):
      nz=vz+dz[i]
      nx=vx+dx[i]
      ny=vy+dy[i]

      if not inRange(nz,nx,ny):
        continue
      if visited[nz][nx][ny]:
        continue
      if graph[nz][nx][ny]==0:
        cnt+=1
        graph[nz][nx][ny]=1  
        q2.append((nz,nx,ny))
  if cnt!=0:
    day+=1 
    bfs(q2)
  else:
    return
  

q=deque()
for k in range(H):
  for i in range(N):
    for j in range(M):
      if graph[k][i][j]==1 and not visited[k][i][j]:
        q.append((k,i,j))  
bfs(q)

for k in range(H):
  for i in range(N):
    if False in visited[k][i]:
      sys.stdout.write(str(-1))
      exit(0)
sys.stdout.write(str(day))