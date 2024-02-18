import sys

R,C=map(int,sys.stdin.readline().split())

A=[list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited=[[False]*C for _ in range(R)]

dx,dy=[-1,0,1],[1,1,1]

def dfs(x,y):
  if y==C-1:
    return True
  for i in range(3):
    nx=x+dx[i]
    ny=y+dy[i]
    
    if not (0<=nx<R and 0<=ny<C):
      continue
    if visited[nx][ny]:
      continue
    if A[nx][ny]=='x':
      continue
    visited[nx][ny]=True

    if dfs(nx,ny):
      return True
  return False
    
  


cnt=0
for r in range(R):
  if dfs(r,0):
    cnt+=1

print(cnt)