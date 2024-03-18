import sys
import heapq

N=int(sys.stdin.readline())
q=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]

q.sort(key=lambda x:(x[1]))
li=[]

for a,b in q:
  heapq.heappush(li,a)
  if len(li)>b:
    heapq.heappop(li)
print(sum(li))