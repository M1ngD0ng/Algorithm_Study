from collections import deque
N=int(input())
M=int(input())

graph=[[] for _ in range(N+1)]

for i in range(M):
  A,B=map(int,input().split())
  graph[A].append(B)
  graph[B].append(A)

cnt=0
def dfs(start):
  global cnt
  visited[start]=True # 지금 방문한 컴퓨터를 visited 처리 함

  for i in graph[start]:
    if visited[i]==False: # 안 가본 곳이면
      visited[i]=True
      cnt+=1
      dfs(i)

  
visited=[False]*(N+1)
dfs(1)
print(cnt)