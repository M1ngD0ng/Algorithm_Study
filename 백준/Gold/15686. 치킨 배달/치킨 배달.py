import sys 
from itertools import combinations

N,M=map(int,sys.stdin.readline().split())
A=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]
chic=[]
home=[]
for i in range(N):
  for j in range(N):
    if A[i][j]==1:
      home.append([i,j])
    elif A[i][j]==2:
      chic.append([i,j])
 
ans=[]

 
for d in combinations(chic,M):
  sumDist=0
  for i,j in home:
    tt=[]
    for x,y in d:
      tt.append(abs(x-i)+abs(y-j))
    sumDist+=min(tt)
  ans.append(sumDist)
print(min(ans))