import sys
from collections import deque

T=int(sys.stdin.readline())
for _ in range(T):
  N,M=map(int,sys.stdin.readline().split())
  A=list(map(int,sys.stdin.readline().split()))

  q=deque()
  for i in range(N):
    q.append((i,A[i]))
  cnt=0
  while q:
    idx,v=q.popleft()
    isPossible=True

    for a,b in q:
      if b>v:
        q.append((idx,v))
        isPossible=False
        break
    if isPossible:
      cnt+=1
    if idx==M and isPossible:
      print(cnt)
      break
    
      