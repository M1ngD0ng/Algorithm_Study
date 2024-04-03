import sys
sys.setrecursionlimit(10**5)

T=int(sys.stdin.readline())

def find(x):
  if parent[x]!=x:
    parent[x]=find(parent[x])
  return parent[x]

def union(a,b):
  a=find(a)
  b=find(b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

  
for t in range(T):
  N=int(sys.stdin.readline())
  K=int(sys.stdin.readline())
  parent=[-1]*(N)

  for i in range(N):
    parent[i]=i

  for _ in range(K):
    a,b=map(int,sys.stdin.readline().split())
    union(a,b)
  
  M=int(sys.stdin.readline())
  
  print(f'Scenario {t+1}:')
  for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    if find(u)==find(v):
      print(1)
    else:
      print(0)
  print()