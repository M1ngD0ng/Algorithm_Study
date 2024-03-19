import sys
import heapq

V,E=map(int,sys.stdin.readline().split())
K=int(sys.stdin.readline())
graph=[[] for _ in range(V+1)]

for _ in range(E):
  a,b,c=map(int,sys.stdin.readline().split())
  graph[a].append((b,c))

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance=[1e8]*(V+1)
  distance[start]=0

  while q:
    dist,now=heapq.heappop(q)

    if distance[now]<dist:
      continue
    for n,d in graph[now]:
      if distance[n]<=(dist+d):
        continue
      distance[n]=dist+d
      heapq.heappush(q,(dist+d,n)) 
  for i in range(1,V+1):
    if distance[i]==1e8:
      print('INF')
    else:
      print(distance[i])
dijkstra(K)