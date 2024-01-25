import sys
from collections import deque

T=int(sys.stdin.readline())

for _ in range(T):
  a,b=map(int,sys.stdin.readline().split())
  dist=b-a
  ans=0
  move=1
  move_plus=0
  while move_plus<dist:
    ans+=1
    move_plus+=move
    if ans%2==0:
      move+=1
  
  print(ans)