T=int(input()) 
dp=[0,1,1,1,2,2,3,4,5,7,9]

for i in range(11,101):
  dp.append(dp[i-5]+dp[i-1])

for _ in range(T):
  t=int(input())
  print(dp[t])