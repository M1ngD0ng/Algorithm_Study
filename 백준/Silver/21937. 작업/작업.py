import sys
sys.setrecursionlimit(10**7)
N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]

for i in range(M):
  A,B=map(int,sys.stdin.readline().split())
  graph[B].append(A)

target=int(input())
visited=[False]*(N+1)
cnt=0
def dfs(start):
  global cnt
  visited[start]=True
  for i in graph[start]:
    if not visited[i]:
      cnt+=1
      dfs(i)

dfs(target)
sys.stdout.write(str(cnt)+'\n')