import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

N=int(sys.stdin.readline())
P=[0]+list(map(int,sys.stdin.readline().split()))
tree=defaultdict(list) 

for _ in range(N-1):
  a,b=map(int,sys.stdin.readline().split())
  tree[a].append(b)
  tree[b].append(a)


visited=[False]*(N+1)

def dfs(node):
  visited[node]=True

  for i in tree[node]:
    if not visited[i]:
      dfs(i)
      dp[node][0]+=max(dp[i][0],dp[i][1])
      dp[node][1]+=dp[i][0]
    

dp=[[0,P[i]] for i in range(N+1)]
visited[1]=True
dfs(1)
print(max(dp[1][0],dp[1][1]))