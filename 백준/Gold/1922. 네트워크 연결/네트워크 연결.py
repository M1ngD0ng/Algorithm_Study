import sys
sys.setrecursionlimit(10**5)

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
cost=[]
for _ in range(M):
  a,b,c=map(int,sys.stdin.readline().split())
  cost.append((a,b,c))

cost.sort(key=lambda x:x[2])

parent=[i for i in range(N+1)]

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

ans=0
for a,b,c in cost:
  if find(a)!=find(b):
    union(a,b)
    ans+=c

print(ans)