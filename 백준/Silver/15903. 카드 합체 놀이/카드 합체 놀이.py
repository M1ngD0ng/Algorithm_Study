import sys
N,M=map(int,sys.stdin.readline().split())

A=list(map(int,sys.stdin.readline().split()))

for i in range(M):
  A.sort()
  temp=A[0]+A[1]
  A[0],A[1]=temp,temp

print(sum(A))