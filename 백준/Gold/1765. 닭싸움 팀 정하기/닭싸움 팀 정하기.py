import sys
from collections import defaultdict

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

friend=defaultdict(set)
enemy=defaultdict(set)



for _ in range(M):
  a,b,c=sys.stdin.readline().split()
  b,c=int(b),int(c)

  if a=='E':
    enemy[b].add(c)
    enemy[c].add(b)
  else:
    friend[b].add(c)
    friend[c].add(b)

def init(idx):
  if friend[idx]:
    for a in list(friend[idx]):
      friend[idx].add(a)

  if enemy[idx]:
    for a in list(enemy[idx]):
        for b in list(enemy[a]):
          if b!=idx:
            friend[idx].add(b)

 
for i in range(1,N+1):
  init(i)
 
def dfs(idx):
  for j in list(friend[idx]):
    if not visited[j]:
      visited[j]=True
      temp.add(j)
      dfs(j)
    
      
ans=[]
for i in range(1,N+1):
  visited=[False]*(N+1)
  visited[i]=True
  temp=set()
  temp.add(i)

  dfs(i)
  if temp not in ans:
    ans.append(temp)

print(len(ans))