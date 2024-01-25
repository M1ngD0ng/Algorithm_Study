import sys
from collections import deque

N=int(sys.stdin.readline())
A=[ list(sys.stdin.readline().rstrip()) for _ in range(N)]


mid=0
def bfs(x,y):
  global mid
  dx,dy=[0,0,1,1,1],[-1,1,0,-1,1]

  for k in range(5):
    nx=dx[k]+x
    if k==3 or k==4:
      nx+=mid
    ny=dy[k]+y
    if not (0<=nx<N and 0<=ny<N):
      sys.stdout.write(str(0)+' ')
      continue
    
  
    cnt=1
    if k==3 or k==4:
      dx[k]=1
      dy[k]=0

    while True:
      nx+=dx[k]
      ny+=dy[k]
      if not (0<=nx<N and 0<=ny<N):
        break
      if A[nx][ny]=='_':
        break
      cnt+=1
    sys.stdout.write(str(cnt)+' ')
    if k==2:
      mid=cnt
  print()


for i in range(N):
  for j in range(N):
    if A[i][j]=='*':
      print(i+2,j+1)
      bfs(i+1,j) # 심장 위치
      sys.exit(0)