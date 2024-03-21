import sys
import heapq

N=int(sys.stdin.readline())
lq,rq=[],[]
for i in range(N):
  a=int(sys.stdin.readline())
  if len(lq)==len(rq):
    heapq.heappush(lq,-a)
  else:
    heapq.heappush(rq,a)

  if i==0:
    print(a)
    continue
  if rq:
    x=-heapq.heappop(lq)
    y=heapq.heappop(rq)
    
    if x>y:
      heapq.heappush(lq,-y)
      heapq.heappush(rq,x)
    else:
      heapq.heappush(lq,-x)
      heapq.heappush(rq,y)
  print(-lq[0])
  