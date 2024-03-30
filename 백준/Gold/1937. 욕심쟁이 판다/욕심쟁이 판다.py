import sys
sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline())

A=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=[[1]*N for _ in range(N)]
visited=[[False]*N for _ in range(N)]
dx,dy=[1,-1,0,0],[0,0,-1,1]

def dfs(x,y):
  for k in range(4):
    nx=dx[k]+x
    ny=dy[k]+y

    if not (0<=nx<N and 0<=ny<N):
      continue
    if A[nx][ny]<=A[x][y]:
      continue
    if visited[nx][ny]:
      dp[x][y]=max(dp[x][y],dp[nx][ny]+1)
      continue
    dp[x][y]=max(dp[x][y],dfs(nx,ny)+1)
  visited[x][y]=True
  return dp[x][y]
    
ans=0
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      ans=max(ans,dfs(i,j))
print(ans)