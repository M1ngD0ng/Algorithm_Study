import sys
from collections import deque

T=int(sys.stdin.readline())
for _ in range(T):
  P=list(sys.stdin.readline().rstrip())
  N=int(sys.stdin.readline())
  temp=sys.stdin.readline().rstrip()
  if N==0:
    temp=[]
  else:
    temp=list(map(int,temp[1:-1].split(',')))
  point=0
  isBreak=False
  for c in P:
    if c=='R':
      if point==0:
        point=-1
      else:
        point=0
    else:
      if not temp:
        isBreak=True
        break
      else:
        temp.pop(point)
  if isBreak:
    print('error')
  else:
    if not temp:
      print('[]')
      continue
    if point==-1:
      temp.reverse()
    for i in range(len(temp)):
      if i==0:
        sys.stdout.write('['+str(temp[i]))
      else:
        sys.stdout.write(','+str(temp[i]))
    sys.stdout.write(']\n')