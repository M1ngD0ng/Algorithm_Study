import sys
from collections import deque

while True:
  s=sys.stdin.readline().rstrip()
  if s=='0 0 0':
    break
  N=list(map(int,s.split()))
  d=dict()

  for i in range(N[0]):
    d[i]=list(map(int,sys.stdin.readline().split()))
  
  idx=[]
  sortKey=sorted(d.keys(),key=lambda x:-abs(d[x][1]-d[x][2]))
  ans=0
  for k in sortKey:
    if d[k][1]>=d[k][2]:
      idx=[2,1]
    else:
      idx=[1,2]
    if N[idx[0]]>=d[k][0]:
      ans+=d[k][0]*d[k][idx[0]]
      N[idx[0]]-=d[k][0] 
    else:
      t1,t2=N[idx[0]],d[k][0]-N[idx[0]]
      if (t1*d[k][idx[0]]+t2*d[k][idx[1]])<(d[k][0]*d[k][idx[1]]):
        ans+=(t1*d[k][idx[0]]+t2*d[k][idx[1]])
        N[idx[0]]-=t1
        N[idx[1]]-=t2
      else:
        ans+=(d[k][0]*d[k][idx[1]])
        N[idx[1]]-=d[k][0]
  print(ans)
