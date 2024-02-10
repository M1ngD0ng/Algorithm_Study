import sys
import heapq

N,M=map(int,sys.stdin.readline().split())

ans=[]
graph=[[] for _ in range(N+1)]
inDegree=[0 for _ in range(N+1)]
q=[]

for i in range(M):
  a,b=map(int,sys.stdin.readline().split())
  graph[a].append(b)
  inDegree[b]+=1

for i in range(1,N+1):
  if inDegree[i]==0:
    heapq.heappush(q,i)

while q:
  v=heapq.heappop(q)
  ans.append(v)

  for i in graph[v]:
    inDegree[i]-=1
    if inDegree[i]==0:
      heapq.heappush(q,i)

print(*ans)