import sys

N=int(sys.stdin.readline())
A=[ int(sys.stdin.readline()) for _ in range(N)]

dp=[0]*N

if len(A)<=2:
  print(sum(A))
else:
  dp[0]=A[0]
  dp[1]=A[0]+A[1]

  for i in range(2,N):
    dp[i]=max(dp[i-3]+A[i-1]+A[i],dp[i-2]+A[i])
  print(dp[-1])