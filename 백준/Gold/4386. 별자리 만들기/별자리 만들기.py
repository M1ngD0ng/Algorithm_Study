import sys
import math

sys.setrecursionlimit(10**5)

N=int(sys.stdin.readline())
A=[]

for _ in range(N):
  a,b=map(float,sys.stdin.readline().split())
  A.append((a,b))

cost=[]

for i in range(N):
  for j in range(N):
    if i==j:
      continue
    cost.append((i,j,math.sqrt((A[i][0]-A[j][0])**2+(A[i][1]-A[j][1])**2)))

cost.sort(key=lambda x:x[2])

parent=[i for i in range(N)]

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