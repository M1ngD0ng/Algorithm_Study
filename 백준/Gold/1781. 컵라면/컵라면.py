import sys
import heapq

N=int(sys.stdin.readline())
A=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
A.sort(key=lambda x:x[0])
q=[]
for d,c in A:
  heapq.heappush(q,c)
  if len(q)>d:
    heapq.heappop(q)

print(sum(q))