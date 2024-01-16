import sys

N=int(sys.stdin.readline())

A=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

sumA=0
for i in range(1,N):
  temp=abs(A[i][0]-A[i-1][0])+abs(A[i][1]-A[i-1][1])
  sumA+=temp

ans=sumA
for i in range(1, N-1):
  a=abs(A[i][0]-A[i-1][0])+abs(A[i][1]-A[i-1][1])
  b=abs(A[i][0]-A[i+1][0])+abs(A[i][1]-A[i+1][1])
  c=abs(A[i-1][0]-A[i+1][0])+abs(A[i-1][1]-A[i+1][1])
  temp=a+b-c
  ans=min(ans,sumA-temp)

print(ans)