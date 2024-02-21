import sys
from collections import deque

T=int(sys.stdin.readline())
for _ in range(T):
  A=deque(sys.stdin.readline().rstrip())

  temp=[]
  canBe=True
  while A:
    t=A.popleft()
    if t=='(':
      temp.append(t)
    else:
      if not temp:
        canBe=False
        break
      if temp[-1]=='(':
        temp.pop()
      else:
        canBe=False
        break
  if temp:
    canBe=False

  if not canBe:
    print('NO')
  else:
    print('YES')