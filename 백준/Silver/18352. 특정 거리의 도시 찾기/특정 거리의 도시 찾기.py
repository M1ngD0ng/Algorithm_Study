import sys
import heapq

N,M,K,X=map(int,sys.stdin.readline().split())
graph=[ [] for _ in range(N+1)]

for _ in range(M):
  a,b=map(int,sys.stdin.readline().split())
  graph[a].append(b)

def dijkstra(start):
  q=[]
  distance=[N+1]*(N+1)
  heapq.heappush(q,(0,start))

  while q: 
    dist,now=heapq.heappop(q)

    if distance[now]<dist: # 이미 방문했던 노드임
      continue
    
    for i in graph[now]:
      if i==start:
        continue
      if dist+1<distance[i]:
        distance[i]=dist+1
        heapq.heappush(q,(dist+1,i))
  for i in range(1,N+1):
    if distance[i]==K:
      print(i)
  if distance.count(K)==0:
    print(-1) 

dijkstra(X)