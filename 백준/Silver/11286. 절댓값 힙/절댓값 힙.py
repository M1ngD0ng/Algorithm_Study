import sys
import heapq

N=int(sys.stdin.readline())
q=[]
for _ in range(N):
  a=int(sys.stdin.readline())
  if a==0:
    if not q:
      print(0)
      continue
    print(heapq.heappop(q)[1])
  else:
    heapq.heappush(q,(abs(a),a))