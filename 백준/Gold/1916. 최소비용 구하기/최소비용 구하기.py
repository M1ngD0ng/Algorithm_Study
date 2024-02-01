import sys
import heapq

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

graph=[[] for _ in range(N+1)]

for _ in range(M):
  a,b,c=map(int,sys.stdin.readline().split())
  graph[a].append((b,c))


start,stop=map(int,sys.stdin.readline().split())

def dijkstra():
  q=[]
  heapq.heappush(q,(start,0))
  distance=[1e8]*(N+1)
  distance[start]=0

  while q:
    now,cnt=heapq.heappop(q)
    if distance[now]<cnt:
      continue

    for i in graph[now]:
      dist=i[1]+cnt
      if dist>=distance[i[0]]:
        continue
      distance[i[0]]=dist
      heapq.heappush(q,(i[0],dist))
  print(distance[stop])
dijkstra()