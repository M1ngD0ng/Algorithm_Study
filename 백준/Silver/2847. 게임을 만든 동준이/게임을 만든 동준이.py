N=int(input())
A=[ int(input()) for _ in range(N)]

A.reverse()
cnt=0
for i in range(1,N):
  if A[i]>=A[i-1]:
    cnt+=(A[i]-A[i-1]+1)
    A[i]=A[i-1]-1

print(cnt)