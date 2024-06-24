import sys
import heapq
V,E=map(int,sys.stdin.readline().split())
K=int(sys.stdin.readline())
graph=[[] for _ in range(V+1)]

for _ in range(E):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(node):
    q=[]
    heapq.heappush(q, (0,node))
    distance=[1e8]*(V+1)
    distance[node]=0

    while q:
        dist,n=heapq.heappop(q)
        if dist>distance[n]:
            continue
        
        for x,y in graph[n]:
            if distance[x]<=dist+y:
                continue
            distance[x]=dist+y
            heapq.heappush(q,(dist+y,x))
    
    for i in range(1,V+1):
        if distance[i]==1e8:
            print('INF')
        else:
            print(distance[i])
    
dijkstra(K)