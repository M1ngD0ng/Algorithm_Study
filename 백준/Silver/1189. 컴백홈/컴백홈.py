import sys
from collections import deque

R,C,K=map(int,sys.stdin.readline().split()) 
A=[ list(map(str,sys.stdin.readline().rstrip())) for _ in range(R)]

ans=0
def dfs(x,y,cnt):
  global ans
  dx,dy=[1,0,-1,0],[0,1,0,-1]
  if cnt==K and x==0 and y==C-1:
    ans+=1
  else:
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if (0<=nx<R and 0<=ny<C) and A[nx][ny]!='T':
        A[nx][ny]='T'
        dfs(nx,ny,cnt+1)
        A[nx][ny]='.' 

A[R-1][0]='T'
dfs(R-1,0,1)  
print(ans) 