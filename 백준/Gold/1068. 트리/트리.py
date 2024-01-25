import sys
from collections import deque

N=int(sys.stdin.readline())
graph=[[] for _ in range(N)]

A=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
root=0
for i in range(N):
  if A[i]==-1:
    root=i
    continue
  graph[A[i]].append(i)

def dfs(node):
  global cnt
  if not graph[node]:
    cnt+=1
  elif len(graph[node])==1 and graph[node][0]==M:
    cnt+=1
  else:
    for i in graph[node]:
      if i==M:
        continue
      dfs(i)




if root==M:
  print(0)
else:
  cnt=0
  dfs(root)
  print(cnt)