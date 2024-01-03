import sys
import heapq

N,M,X=map(int,sys.stdin.readline().split())
graph=[ [] for _ in range(N+1)]

for _ in range(M):
  a,b,c=map(int,sys.stdin.readline().split())
  graph[a].append((b,c))

def dijkstra(start,end):
  q=[]
  heapq.heappush(q,(0,start))
  distance=[int(1e8)]*(N+1)

  while q:
    dist,now=heapq.heappop(q)
    
    if distance[now]<dist:
      continue
    for i in graph[now]:
      if i==start:
        continue
      if dist+i[1]<distance[i[0]]:
        distance[i[0]]=dist+i[1]
        heapq.heappush(q,(dist+i[1],i[0]))
  if start==X and end==X:
    return 0
  else:
    return distance[end]

total=[0]
for i in range(1,N+1):
  t1=dijkstra(i,X)
  t2=dijkstra(X,i)
  total.append(t1+t2)

print(max(total))
