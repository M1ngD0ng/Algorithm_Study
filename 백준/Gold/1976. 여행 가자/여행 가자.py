import sys 
from collections import deque

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())


A=[[] for _ in range(N+1)]
for i in range(N):
  t=list(map(int,sys.stdin.readline().split()))
  for j in range(N):
    if i==j:
      continue
    if t[j]==1:
      A[i+1].append(j+1)

B=list(map(int,sys.stdin.readline().split()))


def bfs(start,end):
  q=deque()
  q.append(start)
  visited=[False]*(N+1)
  visited[start]=True

  while q:   
    v=q.popleft() 
    if v==end:
      return True
    for i in A[v]:
      if not visited[i]:
        visited[i]=True
        q.append(i)
  return False


isPoss=True

if N==1:
  if N in B:
    print('YES')
  else:
    print('NO')
else:
  for i in range(1,M):
    isPoss=bfs(B[i-1],B[i])
    if not isPoss:
      break
  if isPoss:
    print('YES')
  else:
    print('NO')