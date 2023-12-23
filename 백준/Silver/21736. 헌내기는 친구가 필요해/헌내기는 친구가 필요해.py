import sys 
from collections import deque
N,M=map(int,sys.stdin.readline().split())
A=[list(map(str,sys.stdin.readline().rstrip())) for _ in range(N)]
x,y=0,0
for i in range(N):
  for j in range(M):
    if A[i][j]=='I':
      x,y=i,j

cnt=0
def bfs():
  global cnt
  q=deque()
  q.append((x,y))
  visited=[[False]*M for _ in range(N)]
  visited[x][y]=True

  dx,dy=[1,0,-1,0],[0,1,0,-1]
  while q:
    vx,vy=q.popleft()

    for i in range(4):
      nx=vx+dx[i]
      ny=vy+dy[i]
      if not (0<=nx<N and 0<=ny<M):
        continue
      if visited[nx][ny]:
        continue
      if A[nx][ny]=='X':
        visited[nx][ny]=True
        continue
      else:
        visited[nx][ny]=True
        q.append((nx,ny))
        if A[nx][ny]=='0':
          continue
        elif A[nx][ny]=='P':
          cnt+=1

bfs()
if cnt==0:
  print('TT')
else:
  print(cnt)
        