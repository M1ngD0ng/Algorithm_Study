import heapq

def solution(N, road, K):
    graph=[[] for _ in range(N+1)] 
    for r in road:
        graph[r[0]].append([r[1],r[2]])
        graph[r[1]].append([r[0],r[2]])
        
    def dijkstra():
        q=[]
        distance=[1e8]*(N+1)
        heapq.heappush(q, (0,1))

        distance[1]=0
        while q:
            dist, node=heapq.heappop(q)
            
            if dist>distance[node]:
                continue
            
            for nxt, cost in graph[node]:
                if dist+cost>=distance[nxt]:
                    continue
                distance[nxt]=dist+cost
                heapq.heappush(q, (distance[nxt], nxt))
        
        cnt=0
        for d in distance:
            if d<=K:
                cnt+=1
        return cnt
        
    return dijkstra()