import sys

N=int(sys.stdin.readline())
A=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dp=[[0]*3 for _ in range(N)]
for i in range(3):
  dp[0][i]=A[0][i]

for i in range(1,N):
  for j in range(3):
    temp=[]
    for k in range(3):
      if k!=j:
        temp.append(dp[i-1][k]) 
    dp[i][j]=min(temp)+A[i][j]

print(min(dp[N-1]))