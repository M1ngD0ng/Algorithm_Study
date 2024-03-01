import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

ans=[0]*(N+1)
graph=[[] for _ in range(N+1)]
inDegree=[0]*(N+1)
for _ in range(M):
  a,b=map(int,sys.stdin.readline().split())
  inDegree[b]+=1
  graph[a].append(b)

q=deque()
for i in range(1,N+1):
  if inDegree[i]==0:
    q.append((i,1))
    ans[i]=1
 
while q:
  v,cnt=q.popleft()

  for i in graph[v]:
    inDegree[i]-=1
    if inDegree[i]==0:
      q.append((i,cnt+1))
      ans[i]=cnt+1

print(*ans[1:])