import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dx,dy=[0,0,-1,1],[1,-1,0,0]

def bfs(x,y):
  q=deque()
  q.append((x,y))

  visited[x][y]=True

  while q:
    vx,vy=q.popleft()

    for k in range(4):
      nx=vx+dx[k]
      ny=vy+dy[k]
      
      if not (0<=nx<N and 0<=ny<M):
        continue
      if visited[nx][ny]:
        continue
      if arr[nx][ny]==1:
        dp[nx][ny]+=1
        continue
      visited[nx][ny]=True
      q.append((nx,ny))

      
times=0
while True:
  dp=[[0]*M for _ in range(N)]
  visited=[[False]*M for _ in range(N)]
  cnt=0
  cnt2=0
  for i in range(N):
    for j in range(M):
      if arr[i][j]==0 and not visited[i][j]:
        if cnt2==1:
          continue
        cnt2+=1
        bfs(i,j)
      elif arr[i][j]==1:
        cnt+=1

  if cnt==0:
    print(times)
    break
        

  for i in range(N):
    for j in range(M):
      if arr[i][j]==1 and dp[i][j]>1:
        arr[i][j]=0
  times+=1

