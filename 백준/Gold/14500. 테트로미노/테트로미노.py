import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dx=[[0,0,0],[1,2,3],[0,1,1],[1,2,2],[1,2,2],[0,0,1],[0,0,1],[0,1,2],[0,1,2],
    [0,0,-1],[1,1,1],[1,1,2],[1,1,2],[0,-1,-1],[0,1,1],[0,0,1],[-1,0,0],[-1,0,1],[1,1,2]]
dy=[[1,2,3],[0,0,0],[1,0,1],[0,0,1],[0,0,-1],[1,2,0],[1,2,2],[1,0,0],[1,1,1],
    [1,2,2],[0,1,2],[0,1,1],[-1,0,-1],[1,1,2],[1,1,2],[1,2,1],[1,1,2],[1,1,1],[0,1,0]]


ans=0

def bfs(x,y):
  global ans

  for i in range(19):
    cnt=arr[x][y]

    for j in range(3):
      nx=x+dx[i][j]
      ny=y+dy[i][j]

      if not (0<=nx<N and 0<=ny<M):
        cnt=-1
        break
      cnt+=arr[nx][ny]
    
    if cnt!=arr[x][y]:
      ans=max(ans,cnt)
    
  

for i in range(N):
  for j in range(M):
    bfs(i,j)

print(ans)