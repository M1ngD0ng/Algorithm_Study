import sys
from collections import deque

M,N,K=map(int,sys.stdin.readline().split())  
arr=[[0]*M for _ in range(N)]
visited=[[False]*M for _ in range(N)]
ans=[]
for i in range(K):
  a,b,c,d=list(map(int,sys.stdin.readline().split()))
  for j in range(a,c):
    for k in range(b,d):
      arr[j][k]=1
      visited[j][k]=True

def inRange(nx,ny):
  return 0<=nx<N and 0<=ny<M


def bfs(x,y):
  q=deque()
  q.append((x,y))
  dx, dy=[1,0,-1,0],[0,1,0,-1]
  cnt=0
  visited[x][y]=True
  while q:
    ax,ay=q.popleft()
    cnt+=1
    for i in range(4):
      nx=ax+dx[i]
      ny=ay+dy[i]
      if inRange(nx,ny) and not visited[nx][ny]:
        visited[nx][ny]=True
        q.append((nx,ny)) 
  
  ans.append(cnt)

while True:
  for i in range(N):
    for j in range(M):
      if not visited[i][j]:
        bfs(i,j)
      elif (i==N-1 and j==M-1):
        sys.stdout.write(str(len(ans))+'\n')
        ans.sort()
        for k in range(len(ans)):
          sys.stdout.write(str(ans[k])+' ')
        exit(0)