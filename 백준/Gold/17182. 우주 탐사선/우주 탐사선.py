import sys

N,K=map(int,sys.stdin.readline().split())
dp=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

ans=0
for i in range(N):
  for j in range(N):
    for k in range(N):
      dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
   

def dfs(idx,cnt,dist):
  global ans
  if cnt==N:
    ans=min(ans,dist)
  
  else:
    for i in range(N):
      if not visited[i]:
        visited[i]=True
        dfs(i,cnt+1,dist+dp[idx][i])
        visited[i]=False


visited=[False]*N
ans=1e8

visited[K]=True

dfs(K,1,0)
print(ans)