import sys
import heapq

N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
  a,b,c=map(int,sys.stdin.readline().split())
  graph[a].append([b,c])
  graph[b].append([a,c])
  
def dijktra():
  q=[]
  heapq.heappush(q,(1,0))
  dp=[1e8]*(N+1)
  dp[1]=0
  while q:
    v,cnt=heapq.heappop(q)
    
    for a,b in graph[v]: 
      if dp[a]>cnt+b:
        dp[a]=cnt+b
        heapq.heappush(q,(a,cnt+b))
  print(dp[N])

dijktra()