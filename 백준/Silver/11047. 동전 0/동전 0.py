import sys
N,K=map(int,sys.stdin.readline().split())

A=[]
for i in range(N):
  A.append(int(sys.stdin.readline()))

cnt=0
for i in range(N-1,-1,-1):
  if A[i]>K:
    continue
  else:
    cnt+=(K//A[i])
    K%=A[i]
print(cnt)