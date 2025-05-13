import sys
import heapq

N,M,X=map(int,sys.stdin.readline().split())

graph1=[[] for _ in range(N+1)]
graph2=[[] for _ in range(N+1)]

for _ in range(M):
  a,b,c=map(int,sys.stdin.readline().split())
  graph1[a].append((b,c))
  graph2[b].append((a,c))

toX=[1e8]*(N+1)
fromX=[1e8]*(N+1)

def dijkstra(graph, lst):
  q=[]
  heapq.heappush(q,(0,X))
  lst[X]=0

  while q:
    cost, node=heapq.heappop(q)

    for nxt,dist in graph[node]:
      if lst[nxt]>dist+cost:
        lst[nxt]=dist+cost
        heapq.heappush(q,(dist+cost,nxt))

dijkstra(graph1,toX)
dijkstra(graph2,fromX)

ans=0
for i in range(1,N+1):
  ans=max(ans,toX[i]+fromX[i])
print(ans)