import sys

N=int(sys.stdin.readline())
A=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=[[0]*N for _ in range(N)]


def dfs(d,x,y):
  cnt=0
  if d==0:
    if (x,y+1)==(N-1,N-1):
      return 1
    if y+2<N and A[x][y+2]==0:
      cnt+=dfs(0,x,y+1)
    if y+2<N and x+1<N:
      if A[x][y+2]==0 and A[x+1][y+1]==0 and A[x+1][y+2]==0:
        cnt+=dfs(2,x,y+1)
  elif d==1:
    if (x+1,y)==(N-1,N-1):
      return 1
    if x+2<N and A[x+2][y]==0:
      cnt+=dfs(1,x+1,y)
    if x+2<N and y+1<N:
      if A[x+2][y]==0 and A[x+1][y+1]==0 and A[x+2][y+1]==0:
        cnt+=dfs(2,x+1,y)
  else:
    if (x+1,y+1)==(N-1,N-1):
      return 1
    if y+2<N and A[x+1][y+2]==0:
      cnt+=dfs(0,x+1,y+1)
    if x+2<N and A[x+2][y+1]==0:
      cnt+=dfs(1,x+1,y+1)
    if x+2<N and y+2<N:
      if A[x+1][y+2]==0 and A[x+2][y+1]==0 and A[x+2][y+2]==0:
        cnt+=dfs(2,x+1,y+1)
 
  return cnt
  
print(dfs(0,0,0))