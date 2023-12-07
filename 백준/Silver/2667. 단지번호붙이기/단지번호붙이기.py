import sys
from collections import deque

N=int(sys.stdin.readline())
graph=[ list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

visited=[[False]*N for _ in range(N)]

def bfs(x,y):
  q=deque()
  q.append((x,y))
  visited[x][y]=True

  dx=[1,0,-1,0]
  dy=[0,1,0,-1]

  cnt=1
  
  while q:
    vx,vy=q.popleft()

    for i in range(4):
      nx=vx+dx[i]
      ny=vy+dy[i]

      if not (0<=nx<N and 0<=ny<N):
        continue
      if visited[nx][ny]:
        continue

      visited[nx][ny]=True
      
      if graph[nx][ny]==1:
        cnt+=1
        q.append((nx,ny))
  return cnt

ans=[]
while True:
  x,y=-1,-1
  for i in range(N):
    for j in range(N):
      if graph[i][j]==1 and visited[i][j]==False:
        x,y=i,j
        ans.append(bfs(x,y))
  if x==-1 and y==-1:
    break

print(len(ans))
ans.sort()
for i in range(len(ans)):
  print(ans[i])