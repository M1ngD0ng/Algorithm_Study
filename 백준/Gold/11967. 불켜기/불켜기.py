

import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

graph=[[[] for _ in range(N+1)] for _ in range(N+1)]


for _ in range(M):
  x,y,a,b=map(int,sys.stdin.readline().split())
  graph[x][y].append((a,b))

def bfs():
  q=deque()
  q.append((1,1))
  visited=[[False]*(N+1) for _ in range(N+1)]
  visited[1][1]=True

  isOn=[[False]*(N+1) for _ in range(N+1)]
  isOn[1][1]=True

  isPossible=set()
  dx,dy=[0,0,-1,1],[1,-1,0,0]
  cnt=1
  while q: 
    vx,vy=q.popleft()

    for i,j in graph[vx][vy]:
      if not isOn[i][j]:
        isOn[i][j]=True 
        cnt+=1
      if isPossible:
        if (i,j) in isPossible:
          isPossible.remove((i,j))
          visited[i][j]=True
          q.append((i,j))
        
    for i in range(4):
      nx=vx+dx[i]
      ny=vy+dy[i]

      if not (0<nx<=N and 0<ny<=N):
        continue
      if visited[nx][ny]:
        continue
      if not isOn[nx][ny]:
        isPossible.add((nx,ny))
        continue

      visited[nx][ny]=True
      q.append((nx,ny))

  print(cnt)
        

bfs()
    
    