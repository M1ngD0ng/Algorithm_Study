import sys
import heapq

N,D=map(int,sys.stdin.readline().split())
graph=[ [(i+1,1)] for i in range(D+1)]
distance=[D+1]*(D+1)

dp2=[[0,False]]*(D+1) # 여기서 출발하는 지름길이 있는지
for _ in range(N):
  a,b,c=map(int,sys.stdin.readline().split())
  if 0<=a<=D and 0<=b<=D:
    graph[a].append((b,c))

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))

  while q:
    dist,now=heapq.heappop(q)

    if distance[now]<dist:
      continue
    
    if now==D:
      print(dist)
      break
    if now!=D and len(graph[now])==1:
      distance[now+1]=dist+1
      heapq.heappush(q,(dist+1,now+1))
    else: 
      for i in graph[now]:
        if dist+i[1]<distance[i[0]]:
          distance[i[0]]=dist+i[1]
          heapq.heappush(q,(dist+i[1],i[0]))

dijkstra(0)