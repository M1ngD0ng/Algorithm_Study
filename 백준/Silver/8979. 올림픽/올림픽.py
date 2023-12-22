import sys
N,K=map(int,sys.stdin.readline().split())
A=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]

A=sorted(A,reverse=True,key=lambda x:(x[1], x[2], x[3]))

t=1
A[0].append(1)
if N==1:
  print(1)
else:
  for i in range(1,N):
    if A[i][1]!=A[i-1][1]:
      t=i+1
    else:
      if A[i][2]!=A[i-1][2]:
        t=i+1
      else:
        if A[i][3]!=A[i-1][3]:
          t=i+1
    A[i].append(t)
  for i in range(N):
    if A[i][0]==K:
      print(A[i][4])
      break 