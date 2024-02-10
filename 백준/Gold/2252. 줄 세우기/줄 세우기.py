import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(N+1)]
inDegree=[0 for _ in range(N+1)]

for _ in range(M):
  a,b=map(int,sys.stdin.readline().split())
  graph[a].append(b)
  inDegree[b]+=1

q=deque()
for i in range(1,N+1):
  if inDegree[i]==0:
    q.append((i))

ans=[]
while q:
  v=q.popleft()
  ans.append(v)

  for i in graph[v]:
    inDegree[i]-=1
    if inDegree[i]==0:
      q.append((i))

print(*ans)