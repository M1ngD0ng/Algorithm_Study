import sys
import heapq

N,M=map(int,sys.stdin.readline().split())
dp=[[0]*(N+1) for _ in range(N+1)]
graph=[[] for _ in range(N+1)]
for _ in range(M):
  a,b,c=map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

def dijkstra(start):
  q=[]
  distance=[[1e8,0] for _ in range(N+1)]
  distance[start]=[0,'-']

  heapq.heappush(q,(0,start))

  while q:
    dist,now=heapq.heappop(q)
    if distance[now][0]<dist:
      continue

    for n,d in graph[now]:
      if dist+d>=distance[n][0]:
        continue
      distance[n]=[dist+d,now]
      heapq.heappush(q,(distance[n][0],n))
  for i in range(1,N+1):
    dp[i][start]=distance[i][1]
  

for node in range(1,N+1):
  dijkstra(node)

for i in range(1,N+1):
  for j in range(1,N+1):
    sys.stdout.write(str(dp[i][j])+' ')
  print()