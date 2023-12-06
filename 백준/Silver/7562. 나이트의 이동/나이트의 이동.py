import sys
from collections import deque

T=int(sys.stdin.readline())

def bfs(I, iX, iY, tgX, tgY):
  q=deque()
  q.append((iX, iY))

  cntArr=[[0]*I for _ in range(I)]
  
  dx=[-2,-1,1,2,-2,-1,1,2]
  dy=[1,2,2,1,-1,-2,-2,-1]
  visited=[[False]*I for _ in range(I)]
  visited[iX][iY]=True

  while q:
    x, y = q.popleft()
    if x==tgX and y==tgY:
      break

    for i in range(8):
      nx=x+dx[i]
      ny=y+dy[i]

      if not (0<=nx<I and 0<=ny<I):
        continue
      if not visited[nx][ny]:
        visited[nx][ny]=True
        cntArr[nx][ny]=cntArr[x][y]+1
        q.append((nx,ny))
      else: 
        continue 
  return cntArr[tgX][tgY]
          
          

for _ in range(T):
  I=int(sys.stdin.readline())
  iX, iY= map(int,sys.stdin.readline().split())
  tgX, tgY= map(int, sys.stdin.readline().split())
  print(bfs(I, iX, iY, tgX, tgY))

 