import sys
from collections import deque

N=int(sys.stdin.readline())
q=deque()
for _ in range(N):
  s=sys.stdin.readline().rstrip()
  if s[1]=='u': #push
    temp=s.split() 
    q.append(temp[1])
  else:
    lenq=len(q)
    if s[1]=='i': #size
      print(lenq )
    elif s[1]=='m': #empty
      if lenq>0:
        print(0)
      else:
        print(1)
    elif s[1]=='o':
      if lenq==0:
        print(-1)
      else:
        if s[0]=='p': #pop
          print(q.pop())
        elif s[0]=='t': #top
          print(q[lenq-1])