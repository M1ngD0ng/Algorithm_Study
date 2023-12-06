import sys
from collections import deque

F,S,G,U,D=map(int,sys.stdin.readline().split())

def bfs():
  q=deque([S])
  dp=[0]*(F+1)
  visited=[False]*(F+1)
  dp[S]=0
  visited[S]=True
  
  d=[U,-D]
  while q:
    v=q.popleft() 
    if v==G:
      break

    for i in range(2):
      ns=v+d[i]

      if not 1<=ns<=F:
        continue
      if not visited[ns]:
        visited[ns]=True
        dp[ns]=dp[v]+1
        q.append(ns)
      else:
        continue
  if not visited[G]:
    sys.stdout.write('use the stairs')
  else:
    sys.stdout.write(str(dp[G]))

bfs()