import sys
from collections import deque


N,M=map(int,sys.stdin.readline().split())

ans=[]
graph=[[] for _ in range(N+1)]
inDegree=[0 for _ in range(N+1)]
q=deque()

for _ in range(M):
  A=list(map(int,sys.stdin.readline().split()))
  
  for i in range(2,len(A)):
    graph[A[i-1]].append(A[i])
    inDegree[A[i]]+=1
    
for i in range(1,N+1):
  if inDegree[i]==0:
    q.append((i))

while q:
  v=q.popleft()
  ans.append(v)

  for i in graph[v]:
    inDegree[i]-=1
    if inDegree[i]==0:
      q.append((i))

if len(ans)!=N:
  print(0)
else:
  for a in ans:
    print(a)