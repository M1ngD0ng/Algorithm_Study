import sys

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



V,E=map(int,sys.stdin.readline().split())
parent=[i for i in range(V+1)]
cost=[]
for _ in range(E):
  a,b,c=map(int,sys.stdin.readline().split())
  cost.append((a,b,c))

cost.sort(key=lambda x:x[2]) 
ans=0
for a,b,c in cost:
  if find(a)!=find(b):
    ans+=c
    union(a,b)
 
print(ans)