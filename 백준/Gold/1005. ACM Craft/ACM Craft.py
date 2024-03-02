import sys
from collections import deque,defaultdict

T=int(sys.stdin.readline())
for _ in range(T):
  N,K=map(int,sys.stdin.readline().split())
  D=[0]+list(map(int,sys.stdin.readline().split()))

  inDegree=[0]*(N+1)
  dic=defaultdict(list)
  for _ in range(K):
    X,Y=map(int,sys.stdin.readline().split())
    dic[X].append(Y)
    inDegree[Y]+=1

  q=deque()
  ans=[0]*(N+1)
  for i in range(1,N+1):
    if inDegree[i]==0:
      q.append((i))
      ans[i]=D[i]


  while q:
    v=q.popleft()

    for i in dic[v]:
      inDegree[i]-=1
      ans[i]=max(ans[i],ans[v]+D[i])
      if inDegree[i]==0:
        q.append((i))

  W=int(sys.stdin.readline())
  print(ans[W])
