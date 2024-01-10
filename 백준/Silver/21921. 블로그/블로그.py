import sys
from collections import deque

N,X=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
ans=[0]
for i in range(X):
  ans[0]+=A[i]

le,ri=1,X
while True: 
  cnt=ans[le-1]-A[le-1]+A[ri]
  ans.append(cnt)

  le+=1
  ri+=1
  if ri==N:
    break

mA=max(ans)
if mA==0:
  print("SAD")
else:
  print(mA)
  print(ans.count(mA))