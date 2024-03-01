import sys
import heapq

N,V,E=map(int,sys.stdin.readline().split())
A,B=map(int,sys.stdin.readline().split())
H=[0]+list(map(int,sys.stdin.readline().split()))

graph=[[] for _ in range(V+1)]
for _ in range(E):
  a,b,c=map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

ans=[0]*(N+1)

def dijkstra(dest):
  q=[]
  distance=[1e8]*(V+1)
  distance[dest]=0

  heapq.heappush(q,(dest,0))
  while q:
    now,dist=heapq.heappop(q)
    
    if distance[now]<dist:
      continue
  
    for i,j in graph[now]:
      if distance[i]<=dist+j:
        continue
      distance[i]=dist+j
      heapq.heappush(q,(i,distance[i]))
  
  for i in range(1,N+1):
    if distance[H[i]]==1e8:
      ans[i]+=-1
    else:
      ans[i]+=distance[H[i]]

dijkstra(A)
dijkstra(B)

print(sum(ans))