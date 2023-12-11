import sys

N=int(sys.stdin.readline())
dp=[1,1,0,1,1]

for i in range(5,N+1):
  if dp[i-1]+dp[i-4]+dp[i-3]==3:
    dp.append(0)
  else:
    dp.append(1)

if dp[N]:
  print('SK')
else:
  print('CY')