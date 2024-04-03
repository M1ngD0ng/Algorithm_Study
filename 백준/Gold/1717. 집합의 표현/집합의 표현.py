import sys
sys.setrecursionlimit(10**6)

N,M=map(int,sys.stdin.readline().split())
parent=[0]*(N+1)

for i in range(N+1):
  parent[i]=i

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

for _ in range(M):
  c,a,b=map(int,sys.stdin.readline().split())
  if c==0:
    union(a,b)
  else:
    if find(a)==find(b):
      print('YES')
    else:
      print('NO')