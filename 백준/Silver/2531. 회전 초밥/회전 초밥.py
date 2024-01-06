import sys 
from collections import deque

N,d,k,c=map(int,sys.stdin.readline().split())
A=[int(sys.stdin.readline()) for _ in range(N)]


q=deque()
for i in range(k):
  q.append(A[i])

right=k-1
ans=0
while True:  
  s=set(q)
  s.add(c)
  ans=max(ans,len(s))
  if right==k-2:
    break
  q.popleft()
  right+=1
  
  if right==N:
    right=0
  
  q.append(A[right])

print(ans)