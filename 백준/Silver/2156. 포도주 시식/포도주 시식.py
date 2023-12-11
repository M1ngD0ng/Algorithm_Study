import sys

N=int(sys.stdin.readline())
dp=[0]*(N)

arr=[ int(input()) for _ in range(N)]
if N<3:
  print(sum(arr))
else:
  dp[0]=arr[0]
  dp[1]=arr[0]+arr[1] 
  for i in range(2, N):
    mm=max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i]) 
    dp[i]=max(dp[i-1],mm) 
  print(dp[N-1])